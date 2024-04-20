import cv2
import os
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def alter_table(conn, alter_table_sql):
    """ add a new column to the images table """
    try:
        c = conn.cursor()
        c.execute(alter_table_sql)
    except Error as e:
        print(e)

def insert_image(conn, user_images, key_images):
    """ insert an image into the images table """
    sql = ''' INSERT INTO images(user_images, key_images)
              VALUES(?, ?) '''
    cur = conn.cursor()
    with open(user_images, 'rb') as f_user, open(key_images, 'rb') as f_key:
        user_blob = f_user.read()
        key_blob = f_key.read()
    cur.execute(sql, (sqlite3.Binary(user_blob), sqlite3.Binary(key_blob)))
    conn.commit()
    return cur.lastrowid

def capture_key_image():
    # Open the default camera
    cap = cv2.VideoCapture(0)

    # Set the window size
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame', 290, 218)  # Set your desired width and height
    cv2.moveWindow('frame', 487, 290)  # Set your desired x and y coordinates
    cv2.setWindowTitle('frame', 'Key Image')

    count = 1
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the resulting frame
        cv2.imshow('frame', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            filename_user = f'u_img{count}.jpg'
            filename_key = f'key_img{count}.jpg'
            while os.path.exists(filename_user) or os.path.exists(filename_key):
                count += 1
                filename_user = f'u_img{count}.jpg'
                filename_key = f'key_img{count}.jpg'
            # Save the images
            cv2.imwrite(filename_user, frame)
            cv2.imwrite(filename_key, frame)  # This needs to be replaced with actual key image capture
            
            # Store the images in the database
            conn = create_connection("images.db")
            if conn is not None:
                create_table_sql = """ CREATE TABLE IF NOT EXISTS images (
                                        id INTEGER PRIMARY KEY,
                                        user_images TEXT NOT NULL,
                                        key_images TEXT NOT NULL
                                    ); """
                create_table(conn, create_table_sql)
                
                # Alter the table to add the missing column
                alter_table_sql = """ALTER TABLE images ADD COLUMN key_images TEXT NOT NULL DEFAULT '';"""
                alter_table(conn, alter_table_sql)
                
                with conn:
                    insert_image(conn, filename_user, filename_key)
            else:
                print("Error! Cannot create the database connection.")
                
            break

    # Release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_key_image()

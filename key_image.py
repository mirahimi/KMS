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

def insert_image(conn, key_images, user_images):
    """ insert an image into the user_img table """
    sql = ''' INSERT INTO user_img("User Image", "Key Image")
              VALUES(?, ?) '''
    cur = conn.cursor()
    with open(user_images, 'rb') as f1, open(key_images, 'rb') as f2:
        user_image_blob = f1.read()
        key_image_blob = f2.read()
    cur.execute(sql, (sqlite3.Binary(user_image_blob), sqlite3.Binary(key_image_blob)))
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
            user_filename = f'u_img{count}.jpg'
            key_filename = f'k_img{count}.jpg'
            while os.path.exists(user_filename) or os.path.exists(key_filename):
                count += 1
                user_filename = f'u_img{count}.jpg'
                key_filename = f'k_img{count}.jpg'
            # Save the images
            cv2.imwrite(user_filename, frame)
            cv2.imwrite(key_filename, frame)
            
            # Store the images in the database
            conn = create_connection("audit.db")
            if conn is not None:
                create_table_sql = """ CREATE TABLE IF NOT EXISTS user_img (
                                        id INTEGER PRIMARY KEY,
                                        "User Image" BLOB NOT NULL,
                                        "Key Image" BLOB NOT NULL
                                    ); """
                create_table(conn, create_table_sql)
                with conn:
                    insert_image(conn, key_filename, user_filename)
            else:
                print("Error! Cannot create the database connection.")
                
            break

    # Release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_key_image()

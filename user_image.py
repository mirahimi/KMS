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

<<<<<<< HEAD:Frontend/user_image.py
def insert_image(conn, image_file):
    """ insert an image into the images table """
    sql = ''' INSERT INTO images(image)
              VALUES(?) '''
    cur = conn.cursor()
    with open(image_file, 'rb') as f:
=======
def insert_image(conn, user_images):
    """ insert an image into the images table """
    sql = ''' INSERT INTO images("Images")
              VALUES(?) '''
    cur = conn.cursor()
    with open(user_images, 'rb') as f:
>>>>>>> 510484915994fc75ebc6014d114690d7b4986b53:user_image.py
        image_blob = f.read()
    cur.execute(sql, (sqlite3.Binary(image_blob),))
    conn.commit()
    return cur.lastrowid

def capture_user_image():
    # Open the default camera
    cap = cv2.VideoCapture(0)

    # Set the window size
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame', 290, 218)  # Set your desired width and height
    cv2.moveWindow('frame', 487, 290)  # Set your desired x and y coordinates
    cv2.setWindowTitle('frame', 'User Image')

    count = 1
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the resulting frame
        cv2.imshow('frame', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            filename = f'u_img{count}.jpg'
            while os.path.exists(filename):
                count += 1
                filename = f'u_img{count}.jpg'
            # Save the image
            cv2.imwrite(filename, frame)
            
            # Store the image in the database
<<<<<<< HEAD:Frontend/user_image.py
            conn = create_connection("images.db")
            if conn is not None:
                create_table_sql = """ CREATE TABLE IF NOT EXISTS images (
                                        id integer PRIMARY KEY,
                                        image blob NOT NULL
=======
            conn = create_connection("audit.db")
            if conn is not None:
                create_table_sql = """ CREATE TABLE IF NOT EXISTS images (
                                        id INTEGER PRIMARY KEY,
                                        "User Image" BLOB NOT NULL
>>>>>>> 510484915994fc75ebc6014d114690d7b4986b53:user_image.py
                                    ); """
                create_table(conn, create_table_sql)
                with conn:
                    insert_image(conn, filename)
            else:
                print("Error! Cannot create the database connection.")
                
            break

    # Release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_user_image()

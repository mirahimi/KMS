import cv2
import os
import sqlite3
from sqlite3 import Error

# Create a database connection to the SQLite database specified by db_file
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

# Create a table from the create_table_sql statement
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

# Insert an image into the key_img table
def insert_image(conn, key_images):
    sql = ''' INSERT INTO key_img("Key Image")
              VALUES(?) '''
    cur = conn.cursor()
    with open(key_images, 'rb') as f:
        image_blob = f.read()
    cur.execute(sql, (sqlite3.Binary(image_blob),))
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
            filename = f'k_img{count}.jpg'
            while os.path.exists(filename):
                count += 1
                filename = f'k_img{count}.jpg'
            # Save the image
            cv2.imwrite(filename, frame)
            
            # Store the image in the database
            conn = create_connection("audit.db")
            if conn is not None:
                create_table_sql = """ CREATE TABLE IF NOT EXISTS key_img (
                                        id INTEGER PRIMARY KEY,
                                        "Key Image" BLOB NOT NULL
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
    capture_key_image()

# This is the file that needs to be run in order to run the KMS Application

from flask import Flask, render_template, request, redirect
import os
import sqlite3
import datetime

BUILDING_CODES = {
    'Killingsworth Hall': 'HA',
    'Legacy Hall': 'HE',
    'McCullough Trigg Hall': 'CA',
    'Sundance Court': 'HD',
    'Sunwatcher Village': 'CH'
}

# Initialize a Flash Application
app = Flask(__name__)


#-----------------------------------------// 
# USER FUNCTIONS ONLY
#-----------------------------------------//


# Function: Create User Database and Table
def create_user_table():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    # Check if the table already exists
    c.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='users' ''')
    # If the table doesn't exist, create it
    if c.fetchone()[0] != 1:
        c.execute('''CREATE TABLE users
                     (id INTEGER PRIMARY KEY, username TEXT, password TEXT, pin TEXT)''')
        conn.commit()
    conn.close()

# Function: Insert User Credentials into the database
def insert_user(username, password, pin):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    # Check if the user already exists
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    result = c.fetchone()
    # If the user does not exist, insert it
    if result is None:
        c.execute("INSERT INTO users (username, password, pin) VALUES (?, ?, ?)", (username, password, pin))
        conn.commit()
    conn.close()


# Function: Check if User Credentials are valid
def check_credentials(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    result = c.fetchone()
    conn.close()
    return result is not None

# Function: Check if User PIN is valid
def check_pin(username, pin):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND pin = ?", (username, pin))
    result = c.fetchone()
    conn.close()
    return result is not None

#-------------------------------------------//
# KEY FUNCTIONS ONLY
#-------------------------------------------//

# Function: Create Key Database and Table
def create_key_table():
    conn = sqlite3.connect('keys.db')
    c = conn.cursor()
    c.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='keys' ''')
    # If the table doesn't exist, create it
    if c.fetchone()[0] != 1:
        c.execute('''CREATE TABLE keys
                     (building TEXT, roomNum INTEGER, buildingCode TEXT, keyCode INTEGER, keyNum INTEGER, checkedStatus TEXT, authorization INTEGER)''')
        conn.commit()
    conn.close()

# Multiple Functions: Insert All Dorm keys into the database
def insert_kw_keys():
    conn = sqlite3.connect('keys.db')
    c = conn.cursor()

    audit_conn = sqlite3.connect('audit.db')
    audit_c = audit_conn.cursor()

    keyNums = range(1,4)
    buildingCodes = ['HA']
    buildings = ['Killingsworth Hall']
    checkedStatus = 'Checked In'
    authorization = 1

    for i in range(3):  
        keyCode = 1 + i
        roomNum = 1 + i
    
        for keyNum in keyNums:
            for buildingCode in buildingCodes:
                for building in buildings:

                    # Check if the key already exists
                    c.execute("SELECT * FROM keys WHERE building = ? AND roomNum = ? AND buildingCode = ? AND keyCode = ? AND keyNum = ?",
                        (str(building), roomNum, str(buildingCode), keyCode, keyNum))
                    result = c.fetchone()

                    # If the key does not exist, insert it
                    if result is None:
                        c.execute("INSERT INTO keys VALUES (?, ?, ?, ?, ?, ?, ?)",
                            (str(building), roomNum, str(buildingCode), keyCode, keyNum, checkedStatus, authorization))
                    else:

                        # If the checkedStatus has changed, insert a record into audit.db
                        if result[5] != checkedStatus:
                            audit_c.execute("INSERT INTO audit VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                                (str(building), roomNum, str(buildingCode), keyCode, keyNum, checkedStatus, authorization, datetime.datetime.now()))

    conn.commit()
    conn.close()

def insert_lh_keys():
    conn = sqlite3.connect('keys.db')
    c = conn.cursor()

    audit_conn = sqlite3.connect('audit.db')
    audit_c = audit_conn.cursor()

    keyNums = range(1,4)
    buildingCodes = ['HE']
    buildings = ['Legacy Hall']
    checkedStatus = 'Checked In'
    authorization = 1

    for i in range(3):  
        keyCode = 11 + i
        roomNum = 1 + i
    
        for keyNum in keyNums:
            for buildingCode in buildingCodes:
                for building in buildings:

                    # Check if the key already exists
                    c.execute("SELECT * FROM keys WHERE building = ? AND roomNum = ? AND buildingCode = ? AND keyCode = ? AND keyNum = ?",
                        (str(building), roomNum, str(buildingCode), keyCode, keyNum))
                    result = c.fetchone()

                    # If the key does not exist, insert it
                    if result is None:
                        c.execute("INSERT INTO keys VALUES (?, ?, ?, ?, ?, ?, ?)",
                            (str(building), roomNum, str(buildingCode), keyCode, keyNum, checkedStatus, authorization))
                    else:

                        # If the checkedStatus has changed, insert a record into audit.db
                        if result[5] != checkedStatus:
                            audit_c.execute("INSERT INTO audit VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                                (str(building), roomNum, str(buildingCode), keyCode, keyNum, checkedStatus, authorization, datetime.datetime.now()))

    conn.commit()
    conn.close()

def insert_mt_keys():
    conn = sqlite3.connect('keys.db')
    c = conn.cursor()

    audit_conn = sqlite3.connect('audit.db')
    audit_c = audit_conn.cursor()

    keyNums = range(1,4)
    buildingCodes = ['CA']
    buildings = ['McCullough Trigg']
    checkedStatus = 'Checked In'
    authorization = 1

    for i in range(3):  
        keyCode = 21 + i
        roomNum = 1 + i
    
        for keyNum in keyNums:
            for buildingCode in buildingCodes:
                for building in buildings:
                    # Check if the key already exists
                    c.execute("SELECT * FROM keys WHERE building = ? AND roomNum = ? AND buildingCode = ? AND keyCode = ? AND keyNum = ?",
                        (str(building), roomNum, str(buildingCode), keyCode, keyNum))
                    result = c.fetchone()

                    # If the key does not exist, insert it
                    if result is None:
                        c.execute("INSERT INTO keys VALUES (?, ?, ?, ?, ?, ?, ?)",
                            (str(building), roomNum, str(buildingCode), keyCode, keyNum, checkedStatus, authorization))
                    else:

                        # If the checkedStatus has changed, insert a record into audit.db
                        if result[5] != checkedStatus:
                            audit_c.execute("INSERT INTO audit VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                                (str(building), roomNum, str(buildingCode), keyCode, keyNum, checkedStatus, authorization, datetime.datetime.now()))

    conn.commit()
    conn.close()

def insert_sd_keys():
    conn = sqlite3.connect('keys.db')
    c = conn.cursor()

    audit_conn = sqlite3.connect('audit.db')
    audit_c = audit_conn.cursor()

    keyNums = range(1,4)
    buildingCodes = ['HD']
    buildings = ['Sundance Court']
    checkedStatus = 'Checked In'
    authorization = 1

    for i in range(3):  
        keyCode = 31 + i
        roomNum = 1 + i
    
        for keyNum in keyNums:
            for buildingCode in buildingCodes:
                for building in buildings:

                    # Check if the key already exists
                    c.execute("SELECT * FROM keys WHERE building = ? AND roomNum = ? AND buildingCode = ? AND keyCode = ? AND keyNum = ?",
                        (str(building), roomNum, str(buildingCode), keyCode, keyNum))
                    result = c.fetchone()

                    # If the key does not exist, insert it
                    if result is None:
                        c.execute("INSERT INTO keys VALUES (?, ?, ?, ?, ?, ?, ?)",
                            (str(building), roomNum, str(buildingCode), keyCode, keyNum, checkedStatus, authorization))
                    else:

                        # If the checkedStatus has changed, insert a record into audit.db
                        if result[5] != checkedStatus:
                            audit_c.execute("INSERT INTO audit VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                                (str(building), roomNum, str(buildingCode), keyCode, keyNum, checkedStatus, authorization, datetime.datetime.now()))

    conn.commit()
    conn.close()    

def insert_sw_keys():
    conn = sqlite3.connect('keys.db')
    c = conn.cursor()

    audit_conn = sqlite3.connect('audit.db')
    audit_c = audit_conn.cursor()

    keyNums = range(1,4)
    buildingCodes = ['CH']
    buildings = ['Sunwatcher Village']
    checkedStatus = 'Checked In'
    authorization = 1

    for i in range(3):  
        keyCode = 41 + i
        roomNum = 1 + i
    
        for keyNum in keyNums:
            for buildingCode in buildingCodes:
                for building in buildings:

                    # Check if the key already exists
                    c.execute("SELECT * FROM keys WHERE building = ? AND roomNum = ? AND buildingCode = ? AND keyCode = ? AND keyNum = ?",
                        (str(building), roomNum, str(buildingCode), keyCode, keyNum))
                    result = c.fetchone()

                    # If the key does not exist, insert it
                    if result is None:
                        c.execute("INSERT INTO keys VALUES (?, ?, ?, ?, ?, ?, ?)",
                            (str(building), roomNum, str(buildingCode), keyCode, keyNum, checkedStatus, authorization))
                    else:

                        # If the checkedStatus has changed, insert a record into audit.db
                        if result[5] != checkedStatus:
                            audit_c.execute("INSERT INTO audit VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                                (str(building), roomNum, str(buildingCode), keyCode, keyNum, checkedStatus, authorization, datetime.datetime.now()))

    conn.commit()
    conn.close()


#-----------------------------------//
# AUDIT FUNCTIONS ONLY
#-----------------------------------//

def create_audit_table():
    conn = sqlite3.connect('audit.db')
    c = conn.cursor()
    c.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='audit' ''')
    # If the table doesn't exist, create it
    if c.fetchone()[0] != 1:
        c.execute('''CREATE TABLE audit
                     (building TEXT, roomNum INTEGER, buildingCode TEXT, keyCode INTEGER, keyNum INTEGER, checkedStatus TEXT, authorization INTEGER, changeTime TEXT)''')
        conn.commit()
    conn.close()


#-----------------------------------//
# WEB FUNCTIONS ONLY
#-----------------------------------//

# Route for Login Page
@app.route('/')
def login_page():
    return render_template('login_page.html')

# Route for handling Login Credentials: 1st Authentication
@app.route('/login', methods=['POST'])
def login():

    username = request.form['userID']     # Extract Username from the form submitted  
    password = request.form['password']   # Extract Password from the form submitted
    
    if check_credentials(username, password):
        return redirect('/pin')           # If Valid Credentials, redirect to the Pin Page
    else:
        return redirect('/')              # If Invalid Credentials, redirect back to Login Page

# Route for handling "Home" button click
@app.route('/home', methods=['POST','GET'])
def home():
    # Handle the "Home" button action here
    return redirect('/')  # For now, redirect back to the login page

# Route for handling User Registration Form Submission
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        pin = request.form['pin']
        insert_user(username, password, pin)
        return redirect('/')
    else:
        # Handle GET request, maybe render a registration form here
        return render_template('registration_page.html')

# Route for handling Pin Credentials: 2nd Authentication
@app.route('/pin', methods=['GET', 'POST'])
def pin_page():
    if request.method == 'POST':
        username = request.form['userID']
        pin = request.form['pin']
        if check_pin(username, pin):
             return redirect('/keys') # If Valid Credentials, render 'Keys' HTML Template
        else:
            return redirect('/pin')              # If Invalid Credentials, redirect to the Pin Page
    else:
        return render_template('pin_page.html')  # If it's a GET request, render the PIN Page

# Route to render Keys HTML page
@app.route('/keys')
def keys_page():
        return render_template('keys.html')    

# Route to render Pictures HTML page
@app.route('/pictures')
def pictures():
        return render_template('pictures.html')    

# Route to trigger user_image.py execution
@app.route('/capture_user_image')
def capture_user_image():
    # Execute user_image.py using os.system
    os.system("python user_image.py")
    return "User image captured successfully."

# Route to trigger key_image.py execution
@app.route('/capture_key_image')
def capture_key_image():
    # Execute key_image.py using os.system
    os.system("python key_image.py")
    return "Key image captured successfully."

# Route to Confirm Choice
@app.route('/confirm', methods=['POST'])
def confirm():
    housing = request.form['housing']
    room = request.form['room']
    key = request.form['key']
    status = request.form['status']

    print(f"Housing: {housing}, Room: {room}, Key: {key}, Status: {status}")

    # Connect to keys.db
    conn = sqlite3.connect('keys.db')
    c = conn.cursor()

    # Connect to audit.db
    audit_conn = sqlite3.connect('audit.db')
    audit_c = audit_conn.cursor()

    # Check if the key already exists
    c.execute("SELECT * FROM keys WHERE building = ? AND roomNum = ? AND keyNum = ?",
              (str(housing), int(room), int(key)))
    result = c.fetchone()

    # If the key exists
    if result is not None:
        # If the user is trying to check out a key that is already checked out
        if result[5] == 'Checked Out' and status == 'Checked Out':
            audit_c.execute("SELECT changeTime FROM audit WHERE building = ? AND roomNum = ? AND keyNum = ? AND checkedStatus = 'Checked Out' ORDER BY changeTime DESC LIMIT 1",
                            (str(housing), int(room), int(key)))
            last_checkout_time = audit_c.fetchone()[0]
            #last_checkout_str = last_checkout_time.strftime("%Y-%m-%d %H:%M:%S")
            error_message = f"The key for {housing}, Room #{room}, Key #{key} is already checked out. It was last checked out on {last_checkout_time}. Please pick another key."
            return render_template('keys.html', error=error_message)
        # If the user is trying to check in a key that is already checked in
        elif result[5] == 'Checked In' and status == 'Checked In':
            error_message = f"The key for {housing}, Room #{room}, Key #{key} is already checked in! Please pick another key."
            return render_template('keys.html', error=error_message)
        else:
            # Update the checkedStatus in keys.db
            c.execute("UPDATE keys SET checkedStatus = ? WHERE building = ? AND roomNum = ? AND keyNum = ?",
                      (status, str(housing), int(room), int(key)))
            conn.commit()
            conn.close()

            # Connect to audit.db
            audit_conn = sqlite3.connect('audit.db')
            audit_c = audit_conn.cursor()

            # Insert a record into audit.db
            audit_c.execute("INSERT INTO audit VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                            (result[0], result[1], result[2], result[3], result[4], status, result[6], datetime.datetime.now()))
            audit_conn.commit()
            audit_conn.close()

            # Redirect to the image capture page
            return render_template('confirmation.html', housing=housing, room=room, key=key, status=status)


# Main block to execute when this script is run
if __name__ == '__main__':
    create_user_table()                          # Create user table if it doesn't exist
    create_key_table()                           # Create key table if it doesn't exist
    create_audit_table()                         # Create audit table if it doesn't exist
    insert_user('chintan', 'admin', '123')       # Insert sample user data
    insert_user('sly', 'admin', '456')
    insert_user('m1', 'p1', '111') 
    insert_user('m2', 'p2', '222')
    insert_user('m3', 'p3', '333')
    insert_user('m4', 'p4', '444')
    insert_user('m5', 'p5', '555')
    insert_kw_keys()
    insert_lh_keys()
    insert_mt_keys()
    insert_sd_keys()
    insert_sw_keys()

    app.run(debug=True)                          # Run Flask App in Debug Mode
    
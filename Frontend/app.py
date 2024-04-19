# This is the file that needs to be run in order to run the KMS Application

from flask import Flask, render_template, request, redirect
import sqlite3

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

# Function: Insert keys into the database

def insert_kw_keys():
    conn = sqlite3.connect('keys.db')
    c = conn.cursor()

    keyNums = range(1,4)
    buildingCodes = ['HA']
    buildings = ['Killingsworth Hall']
    checkedStatus = 'Checked In'
    authorization = 1

    for i in range(11):  
        keyCode = 300 + i
        roomNum = 100 + i
    
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

    conn.commit()
    conn.close()

def insert_lh_keys():
    conn = sqlite3.connect('keys.db')
    c = conn.cursor()

    keyNums = range(1,4)
    buildingCodes = ['HE']
    buildings = ['Legacy Hall']
    checkedStatus = 'Checked In'
    authorization = 1

    for i in range(11):  
        keyCode = 400 + i
        roomNum = 100 + i
    
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

    conn.commit()
    conn.close()

def insert_mt_keys():
    conn = sqlite3.connect('keys.db')
    c = conn.cursor()

    keyNums = range(1,4)
    buildingCodes = ['CA']
    buildings = ['McCullough Trigg']
    checkedStatus = 'Checked In'
    authorization = 1

    for i in range(11):  
        keyCode = 500 + i
        roomNum = 100 + i
    
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

    conn.commit()
    conn.close()

def insert_sd_keys():
    conn = sqlite3.connect('keys.db')
    c = conn.cursor()

    keyNums = range(1,4)
    buildingCodes = ['HD']
    buildings = ['Sundance Court']
    checkedStatus = 'Checked In'
    authorization = 1

    for i in range(11):  
        keyCode = 600 + i
        roomNum = 100 + i
    
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

    conn.commit()
    conn.close()    

def insert_sw_keys():
    conn = sqlite3.connect('keys.db')
    c = conn.cursor()

    keyNums = range(1,4)
    buildingCodes = ['CH']
    buildings = ['Sunwatcher Village']
    checkedStatus = 'Checked In'
    authorization = 1

    for i in range(11):  
        keyCode = 700 + i
        roomNum = 100 + i
    
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

    conn.commit()
    conn.close()


#-----------------------------------//
# AUDIT FUNCTIONS ONLY
#-----------------------------------//

    

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
             return render_template('keys.html') # If Valid Credentials, render 'Keys' HTML Template
        else:
            return redirect('/pin')              # If Invalid Credentials, redirect to the Pin Page
    else:
        return render_template('pin_page.html')  # If it's a GET request, render the PIN Page

# Route for Confirming User's Selection
@app.route('/confirm', methods=['POST'])
def confirm():
    housing = request.form['housing']
    room = request.form['room']
    key = request.form['key']
    
    # Process the selected housing, room, and key options
    selection = f"<b>You have selected:</b> <br/> \
                 <b>Housing:</b> {housing}<br/> \
                 <b>Room:</b> {room}<br/> \
                 <b>Key:</b> {key}"
    
        # Render a new template or return the selection as a response
    return selection




# Main block to execute when this script is run
if __name__ == '__main__':
    create_user_table()                          # Create user table if it doesn't exist
    create_key_table()                           # Create key table if it doesn't exist
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
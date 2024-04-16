# This is the file that needs to be run in order to run the KMS Application

from flask import Flask, render_template, request, redirect
import sqlite3

# Initialize a Flash Application
app = Flask(__name__)


# Function: Create Database and Table
def create_table():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, username TEXT, password TEXT, pin TEXT)''')
    conn.commit()
    conn.close()

# Function: Insert User Credentials into the database
def insert_user(username, password, pin):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
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
    create_table()                               # Create table if it doesn't exist
    insert_user('user1', 'abc', '123')           # Insert sample user data (for demonstration purposes)
    insert_user('user2', 'xyz', '789')
    app.run(debug=True)                          # Run Flask App in Debug Mode
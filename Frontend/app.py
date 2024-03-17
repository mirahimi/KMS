from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


# Function to create database and table if they don't exist
def create_table():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, username TEXT, password TEXT, pin TEXT)''')
    conn.commit()
    conn.close()


# Function to insert user credentials into the database
def insert_user(username, password, pin):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password, pin) VALUES (?, ?, ?)", (username, password, pin))
    conn.commit()
    conn.close()

# Function to check if user credentials are valid
def check_credentials(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    result = c.fetchone()
    conn.close()
    return result is not None

# Function to check if user PIN is valid
def check_pin(username, pin):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND pin = ?", (username, pin))
    result = c.fetchone()
    conn.close()
    return result is not None

@app.route('/')
def login_page():
    return render_template('login_page.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['userID']
    password = request.form['password']
    
    if check_credentials(username, password):
        return redirect('/pin')
    else:
        return redirect('/')

@app.route('/confirm', methods=['POST'])
def confirm():
    selected_room = request.form['room']
    return f'Your choice is: {selected_room}'

@app.route('/pin', methods=['GET', 'POST'])
def pin_page():
    if request.method == 'POST':
        username = request.form['userID']
        pin = request.form['pin']
        if check_pin(username, pin):
             return render_template('keys.html')
#            return render_template('welcome.html', username=username)
        else:
            return redirect('/pin')
    else:
        return render_template('pin_page.html')


if __name__ == '__main__':
    create_table()  # Create table if it doesn't exist
    # Insert sample user data (for demonstration purposes)
    insert_user('user1', 'abc', '123')
    insert_user('user2', 'xyz', '789')
    app.run(debug=True)

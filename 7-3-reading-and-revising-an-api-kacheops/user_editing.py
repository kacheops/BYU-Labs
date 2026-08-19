from flask import Flask, request, jsonify
import json
import sqlite3

app = Flask(__name__)

@app.route('/')  # The root/Index of the server
def home():
    #TODO: Return a string that will be displayed on the home page
    return '''<span style='text-align:center'>
                <h1>K.Ache Ops Sysadmin</h1>
                <h3>Official Database Management</h3><hr/>
            </span>'''

@app.route('/revise')  # domain/revise route
def edit_request():
    username = request.args.get('username')  # URL is of form http://domain/revise?username=x
    auth = request.args.get('auth')  # URL is of form http://domain/revise?username=x&auth=value

    #TODO: Implement the logic to handle the request
    # create the control flow to handle the request
    # if the username is not provided, return an error message
    
    if not username:
        return jsonify({'error': 'Username is required, Please provide a username.'}), 404

    user_record = access_row(username)

    # if the username is provided but the auth is not, return the user record
    
    if user_record is None:
        return jsonify({'error': 'User not found.'}), 400

    if auth is None:
        return jsonify({
            "user_id": user_record[0],
            "username": user_record[1],
            "password": user_record[2],
            "auth_level": user_record[3]   
        })

    # if the username and auth are provided, update the user record and return the updated record
    
    update_auth(username, auth)

    # if the username is not found, return an error message
    
    user_record = access_row(username)

    # do not forget to return the response as a JSON object
    
    return jsonify({
        "user_id": user_record[0],
        "username": user_record[1],
        "password": user_record[2],
        "auth_level": user_record[3]
    })

def access_row(person):
    #TODO: update the database connection and query to return the user record
    conn = sqlite3.connect('people.db')  # TO-DO: Change '' to the database name inside quotes, Hint: the name ends with .db
    cursor = conn.cursor()  # Get cursor
    cursor.execute("SELECT * FROM users WHERE username = ?", (person,))  # Read SQL
    user_record = cursor.fetchone()  # Get row
    conn.close()  # Release resources
    return user_record  # Got a record


def update_auth(person, auth):  # Delegate the updating to this function
    #TODO: update the database connection and query to update the user record
    conn = sqlite3.connect('people.db')  # TO-DO: Change '' to the database name inside quotes, Hint: the name ends with .db
    cursor = conn.cursor()  # Get cursor
    result = cursor.execute('''UPDATE users SET auth_level=? WHERE username = ?''', (auth, person))
    conn.commit()  # Make changes permanent
    conn.close()  # Release resources
    return result

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, jsonify, request
import sqlite3
 
app = Flask(__name__)

def create_database():
    conn = sqlite3.connect('users.db') 
    
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT
    )
    ''')

    conn.commit()

    conn.close()

@app.route('/account', methods=["POST"])
def create_account():    
    request_json = request.get_json()
    try: 
        username = request_json["username"]
        password = request_json["password"]
    except:
        return "", 400
    return jsonify({"naofixe": username, "fixe": password})

 
if __name__ == '__main__':
    app.run(debug=True)
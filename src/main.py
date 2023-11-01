from flask import Flask, jsonify, request
import sqlite3
import json
from accounts.create import create_user

with open("config.json", "r") as f:
    config = json.load(f)
 
app = Flask(__name__)

connection = sqlite3.connect(config["database_file"])

@app.route('/account', methods=["POST"])
def create_account():    
    request_json = request.get_json()
    try: 
        username = request_json["username"]
        password = request_json["password"]
    except:
        return "", 400
    cursor = connection.cursor
    create_user(cursor)
    create_user(cursor)
    create_user(cursor)
    create_user(cursor)
    cursor.commit()
    return jsonify({"naofixe": username, "fixe": password})

 
if __name__ == '__main__':
    app.run(debug=True)
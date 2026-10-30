from flask import Flask, request
import sqlite3
import hashlib

app = Flask(__name__)

@app.route("/hash")
def voir_hash():
    conn = sqlite3.connect("users.db")
    user = conn.execute("SELECT * FROM users WHERE username='admin'").fetchone()
    conn.close()
    return f"""
        Mot de passe en clair : {user[2]}<br>
        Mot de passe MD5 : {user[3]}
    """

if __name__ == "__main__":
    app.run(debug=True)
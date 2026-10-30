from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/login")
def login():
    username = request.args.get("username")
    password = request.args.get("password")

    conn = sqlite3.connect("users.db")
    # vulnerable
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    result = conn.execute(query).fetchone()
    """
    SOLUTION
    query = "SELECT * FROM users WHERE username=? AND password=?"
    result = conn.execute(query, (username, password)).fetchone()
    """
    conn.close()

    if result:
        return f"Connecté en tant que : {result[1]}"
    return "Accès refusé"

if __name__ == "__main__":
    app.run(debug=True)
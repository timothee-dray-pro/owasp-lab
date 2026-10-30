from flask import Flask, request

app = Flask(__name__)

users = {
    "admin": "supersecret"
}

@app.route("/login")
def login():
    username = request.args.get("username")
    password = request.args.get("password")

    # vulnerable
    if users.get(username) == password:
        return f"Connecte en tant que {username}"
    return "Acces refuse", 403

if __name__ == "__main__":
    app.run(debug=True)
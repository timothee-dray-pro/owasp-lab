from flask import Flask, request, session

app = Flask(__name__)
app.secret_key = "cle-secrete-tres-longue"  # signe les cookies

# Faux utilisateurs
users = {
    "alice": {"password": "1234", "role": "user"},
    "bob": {"password": "5678", "role": "admin"}
}

@app.route("/login")
def login():
    username = request.args.get("username")
    password = request.args.get("password")
    user = users.get(username)
    if user and user["password"] == password:
        session["username"] = username
        session["role"] = user["role"]  # role stocke cote serveur
        return f"Connecte en tant que {username} ({user['role']})"
    return "Acces refuse", 403

@app.route("/public")
def public():
    return "Page publique - accessible a tous"

@app.route("/user")
def user():
    if session.get("role") in ["user", "admin"]:
        return f"Page utilisateur - bonjour {session['username']}"
    return "Acces refuse", 403

@app.route("/admin")
def admin():
    # vulerable
    role = request.args.get("role")
    if role == "admin":
        return "Panel admin - donnees sensibles"
    return "Acces refuse", 403

    """
    SOLUTION

    if session.get("role") == "admin":
        return f"Panel admin - bienvenue {session['username']}"
    return "Acces refuse", 403
    """

if __name__ == "__main__":
    app.run(debug=True)
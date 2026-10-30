from flask import Flask, request
import logging

app = Flask(__name__)

# ✅ Logger dédié, pas le logger racine
auth_logger = logging.getLogger("auth")
auth_logger.setLevel(logging.WARNING)
handler = logging.FileHandler("auth.log")
handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
auth_logger.addHandler(handler)
auth_logger.propagate = False  # empêche la remontée vers le logger racine

users = {"admin": "supersecret"}

@app.route("/login")
def login():
    username = request.args.get("username")
    password = request.args.get("password")
    ip = request.remote_addr

    if users.get(username) == password:
        auth_logger.info(f"SUCCES login | user={username} | ip={ip}")
        return f"Connecté en tant que {username} ✅"
    auth_logger.warning(f"ECHEC login | user={username} | ip={ip}")
    return "Accès refusé ❌", 403

if __name__ == "__main__":
    app.run(debug=True)
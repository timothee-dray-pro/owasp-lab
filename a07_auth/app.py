from flask import Flask, request
from collections import defaultdict
import time

app = Flask(__name__)

# Mot de passe volontairement faible
users = {
    "admin": "1234"
}

# Stocke les tentatives : {ip: [timestamp, timestamp, ...]}
tentatives = defaultdict(list)

MAX_TENTATIVES = 3
FENETRE = 60  # secondes

@app.route("/login")
def login():
    ip = request.remote_addr
    maintenant = time.time()

    """
    SOLUTION

    tentatives[ip] = [t for t in tentatives[ip] if maintenant - t < FENETRE]
    
    if len(tentatives[ip]) >= MAX_TENTATIVES:
        return f"Trop de tentatives — réessaie dans {FENETRE}s", 429

    tentatives[ip].append(maintenant)
    """
    
    username = request.args.get("username")
    password = request.args.get("password")

    if users.get(username) == password:
        return f"Connecte en tant que {username}"
    return "Acces refuse", 403

if __name__ == "__main__":
    app.run(debug=True)
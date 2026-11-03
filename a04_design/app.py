from flask import Flask, request
import random

app = Flask(__name__)

# Stocke les tokens de reset en mémoire : {username: token}
reset_tokens = {}

@app.route("/reset-request")
def reset_request():
    username = request.args.get("username")
    # vulnerable car prévisible
    token = str(random.randint(1000, 9999))
    reset_tokens[username] = token
    # Normalement envoyé par email — ici on l'affiche pour simuler
    return f"Token envoyé par email à {username} (simulation) : {token}"

@app.route("/reset-confirm")
def reset_confirm():
    username = request.args.get("username")
    token = request.args.get("token")
    nouveau_mdp = request.args.get("nouveau_mdp")

    # ⚠️ VULNÉRABLE : pas d'expiration, pas de limite de tentatives
    if reset_tokens.get(username) == token:
        return f"Mot de passe de {username} changé en : {nouveau_mdp} ✅"
    return "Token invalide", 403

if __name__ == "__main__":
    app.run(debug=True)
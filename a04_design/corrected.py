from flask import Flask, request
import secrets
import time

app = Flask(__name__)

# {username: (token, timestamp)}
reset_tokens = {}

EXPIRATION = 300  # 5 minutes

@app.route("/reset-request")
def reset_request():
    username = request.args.get("username")
    # Token long et aléatoire cryptographiquement sûr
    token = secrets.token_urlsafe(16)
    reset_tokens[username] = (token, time.time())
    return f"Token envoyé par email à {username} (simulation) : {token}"

@app.route("/reset-confirm")
def reset_confirm():
    username = request.args.get("username")
    token = request.args.get("token")
    nouveau_mdp = request.args.get("nouveau_mdp")

    if username not in reset_tokens:
        return "Aucune demande de reset en cours", 403

    token_stocke, timestamp = reset_tokens[username]

    # Durée de temps du token
    if time.time() - timestamp > EXPIRATION:
        del reset_tokens[username]
        return "Token expiré", 403

    if token_stocke == token:
        del reset_tokens[username]
        return f"Mot de passe de {username} changé en : {nouveau_mdp}"
    return "Token invalide", 403

if __name__ == "__main__":
    app.run(debug=True)
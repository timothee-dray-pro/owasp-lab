from flask import Flask, request
import requests

app = Flask(__name__)

WHITELIST = ["example.com", "api.monservice.com"]

# Route cachee (en vraie non car tout est sur la meme machine) interne
@app.route("/admin")
def admin():
    return "Panel admin secret - reserve au serveur interne"

# vulnerable
@app.route("/fetch")
def fetch():
    url = request.args.get("url")

    """
    SOLUTION
    domaine = urlparse(url).hostname

    if domaine not in WHITELIST:
        return f"Domaine non autorise : {domaine}", 403
    """
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    app.run(debug=True)
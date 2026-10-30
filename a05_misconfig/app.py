from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Bienvenue sur l'app"

@app.route("/erreur")
def erreur():
    # Declenche une erreur volontaire pour tester
    x = 1 / 0
    return str(x)

if __name__ == "__main__":
    # vulnerable
    app.run(debug=True)

    """
    SOLUTION

    app.run(debug=False)
    """
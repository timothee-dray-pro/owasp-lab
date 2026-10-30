# OWASP Lab — Flask

Lab pratique pour comprendre et exploiter les failles OWASP Top 10.

---

## A03 — Injection SQL

**Principe :** une requête SQL construite avec des données utilisateur permet à un attaquant de modifier la logique de la requête.

**Exploit :**
/login?username=' OR 1=1--&password=x

→ connecté en tant qu'admin sans connaître le mot de passe.

**Correction :** requêtes paramétrées (`?` placeholders) — les données ne sont jamais interprétées comme du SQL.

---

## A10 — SSRF (Server-Side Request Forgery)

**Principe :** le serveur fait une requête HTTP vers une URL fournie par l'utilisateur, ce qui permet d'atteindre des ressources internes normalement inaccessibles.

**Exploit :**
/fetch?url=http://127.0.0.1:5000/admin
→ le serveur visite lui-même son panel interne à notre place.

**Correction :** whitelist des domaines autorisés — toute URL hors liste est rejetée.

# OWASP Lab — Flask

Lab pratique pour comprendre et exploiter les failles OWASP Top 10.

---

## A01 — Broken Access Control

**Principe :** le serveur fait confiance à des données envoyées par le client (paramètre URL, cookie) pour déterminer les droits d'accès.

**Exploit :**
/admin?role=admin

→ n'importe qui accède au panel admin en se déclarant admin dans l'URL.

**Correction :** stocker le rôle dans une session côté serveur — le client ne peut pas la modifier.

## A02 — Cryptographic Failures

**Principe :** stocker des mots de passe en clair ou avec MD5 expose les utilisateurs si la base est volée.

**Exploit :** hash MD5 de "1234" → `81dc9bdb52d04dc20036dbd8313ed055`  
Collé sur crackstation.net → cracké en moins d'une seconde via rainbow tables.

**Correction :** bcrypt avec sel intégré et coût 12 — lent par design, plus résistant

## A03 — Injection SQL

**Principe :** une requête SQL construite avec des données utilisateur permet à un attaquant de modifier la logique de la requête.

**Exploit :**
/login?username=' OR 1=1--&password=x

→ connecté en tant qu'admin sans connaître le mot de passe.

**Correction :** requêtes paramétrées (`?` placeholders) — les données ne sont jamais interprétées comme du SQL.

---

## A05 — Security Misconfiguration

**Principe :** `debug=True` en production expose le code source, les chemins de fichiers et une console Python interactive.

**Exploit :** une erreur volontaire (`1/0`) affiche la stack trace complète avec le code source et un accès console au serveur.

**Correction :** `debug=False` + gestion d'erreur générique — aucune information interne n'est exposée.

## A07 — Authentication Failures

**Principe :** aucune limite sur les tentatives de connexion permet à un attaquant de tester des milliers de mots de passe automatiquement.

**Exploit :** script Python qui teste une wordlist → mot de passe "1234" trouvé en 4 essais.

**Correction :** rate limiting — max 3 tentatives par IP sur 60 secondes, réponse 429 au-delà.

## A10 — SSRF (Server-Side Request Forgery)

**Principe :** le serveur fait une requête HTTP vers une URL fournie par l'utilisateur, ce qui permet d'atteindre des ressources internes normalement inaccessibles.

**Exploit :**
/fetch?url=http://127.0.0.1:5000/admin
→ le serveur visite lui-même son panel interne à notre place.

**Correction :** whitelist des domaines autorisés — toute URL hors liste est rejetée.

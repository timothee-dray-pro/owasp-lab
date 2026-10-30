import bcrypt

mot_de_passe = "1234"

# Genere un sel et hache
sel = bcrypt.gensalt()
hash_bcrypt = bcrypt.hashpw(mot_de_passe.encode(), sel)

print(f"Mot de passe : {mot_de_passe}")
print(f"Hash bcrypt  : {hash_bcrypt.decode()}")

# Verification
correct = bcrypt.checkpw("1234".encode(), hash_bcrypt)
mauvais = bcrypt.checkpw("azerty".encode(), hash_bcrypt)

print(f"\nVerif '1234'   → {correct}")
print(f"Verif 'azerty' → {mauvais}")
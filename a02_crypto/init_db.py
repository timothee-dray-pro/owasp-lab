import sqlite3
import hashlib

conn = sqlite3.connect("users.db")
conn.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password_clair TEXT,
        password_md5 TEXT
    )
""")

md5 = hashlib.md5("1234".encode()).hexdigest()
conn.execute("INSERT OR IGNORE INTO users VALUES (1, 'admin', '1234', ?)", (md5,))
conn.commit()
conn.close()
print("Base cree.")
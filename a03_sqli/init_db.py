import sqlite3

conn = sqlite3.connect("users.db")
conn.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT
    )
""")
conn.execute("INSERT INTO users VALUES (1, 'admin', 'supersecret')")
conn.commit()
conn.close()
print("Base créée.")
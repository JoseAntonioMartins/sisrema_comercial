import sqlite3

conn = sqlite3.connect("store.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Username TEXT NOT NULL,
    Email TEXTO NOT NULL,
    Password TEXT NOT NULL,
    ConfPassword TEXT NOT NULL
)""")

print("Conexão ao banco de dados feita com sucesso!")
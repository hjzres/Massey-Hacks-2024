import sqlite3

DATABASE = 'db.sqlite3'

with open("create_tables.sql", 'r') as sql_file:
    script = sql_file.read()

conn = sqlite3.connect(DATABASE)

cursor = conn.cursor()
cursor.executescript(script)
conn.commit()

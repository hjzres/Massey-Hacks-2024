from mh2024 import crud


with open("create_tables.sql", 'r') as sql_file:
    script = sql_file.read()

cursor = crud.get_db().cursor()
cursor.executescript(script)
crud.get_db().commit()

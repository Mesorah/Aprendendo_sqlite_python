import sqlite3
from pathlib import Path

DB_NAME = 'meu_sql.sqlite'
DB_ROOT = Path(__file__).parent
DB_FILE = DB_ROOT / DB_NAME
TABLE_NAME = 'TEST'

nome_pessoa = input('qual seu nome? ')
peso_pessoa = int(input('qual seu peso? '))

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')')
connection.commit()

cursor.execute(f'INSERT INTO TEST (name, weight) VALUES (?, ?)', (nome_pessoa, peso_pessoa))
connection.commit()

cursor.close()
connection.close()
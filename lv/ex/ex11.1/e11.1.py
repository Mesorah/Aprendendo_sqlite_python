import sqlite3
from contextlib import closing
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
print(DB_FILE)

with sqlite3.connect(DB_FILE) as conexao:
    with closing(conexao.cursor()) as cursor:
        # cursor.execute('CREATE TABLE IF NOT EXISTS precos(nome text, preco real)')
        # cursor.execute('INSERT INTO precos(nome, preco) VALUES (?,?)', ('Carlin', 400))
        # conexao.commit()

        cursor.execute('SELECT * FROM precos')
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                break

            print(f'Nome: {resultado[0]}\nDinheiro: {resultado[1]}\n')

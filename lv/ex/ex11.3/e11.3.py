import sqlite3
from contextlib import closing
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
DB_NAME = 'ex11.1\db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME

v1 = int(input('v1: '))
v2 = int(input('v2: '))

with sqlite3.connect(DB_FILE) as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('SELECT * FROM precos Where preco BETWEEN ? AND ?', (v1, v2))

        n = 0
        while True:
            resultado = cursor.fetchone()

            if resultado is None:
                if n == 0:
                    print('Nada encontrado')
                break

            print(f'Nome: {resultado[0]}\nPreço: {resultado[1]}\n')
            n += 1
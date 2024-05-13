import sqlite3
from contextlib import closing
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_FILE = ROOT_DIR / 'agenda.db'

with sqlite3.connect(DB_FILE) as conexao:
    conexao.row_factory = sqlite3.Row
    for registro in conexao.execute('SELECT * FROM agenda'):
        print(f'Nome: {registro['nome']}\nTelefone: {registro['telefone']}\n')
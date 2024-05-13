import sqlite3
from contextlib import closing
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
DB_NAME = 'ex11.1\db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME

with sqlite3.connect(DB_FILE) as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('UPDATE precos SET preco = preco * 1.10')
        conexao.commit()
import sqlite3
from contextlib import closing
from pathlib import Path

ARQUIVO_BRUTO = Path(__file__).parent
NOME_BANCO = 'brasil.db'
ARQUIVO_COMPLETO = ARQUIVO_BRUTO / NOME_BANCO

with sqlite3.connect(ARQUIVO_COMPLETO) as connection:
    connection.row_factory = sqlite3.Row
    print(f'{"Id":3s} {"Estados":<20s} {"População":12s}')
    print('=' * 37)
    for estado in connection.execute('SELECT * FROM estados order by nome'):
        print(f'{estado["id"]:3d} {estado["nome"]:<20s} {estado["populacao"]:12d}')
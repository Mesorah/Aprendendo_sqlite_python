import sqlite3
from contextlib import closing
from pathlib import Path

ARQUIVO_BRUTO = Path(__file__).parent.parent
NOME_BANCO = 'gerando_chave_primária\\brasil.db'
ARQUIVO_COMPLETO = ARQUIVO_BRUTO / NOME_BANCO

with sqlite3.connect(ARQUIVO_COMPLETO) as connection:
    for feriado in connection.execute('SELECT * FROM feriados'):
        print(feriado)
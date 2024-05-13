import sqlite3
from contextlib import closing
from pathlib import Path

ARQUIVO_BRUTO = Path(__file__).parent.parent
NOME_BANCO = 'gerando_chave_primária\\brasil.db'
ARQUIVO_COMPLETO = ARQUIVO_BRUTO / NOME_BANCO

feriados = [
    ["2018-01-01", "Confraternização Universal"],
    ["2018-04-21", "Tiradentes"],
    ["2018-05-01", "Dia do Trabalho"],
    ["2018-09-07", "Independência do Brasil"],
    ["2018-10-12", "Nossa Senhora Aparecida"],
    ["2018-11-02", "Finados"],
    ["2018-11-15", "Proclamação da República"],
    ["2018-12-25", "Natal"],
]



with sqlite3.connect(ARQUIVO_COMPLETO) as connection:
    connection.execute('CREATE TABLE feriados(id integer primary key autoincrement, data date, descricao text)')
    connection.executemany('INSERT INTO feriados(data, descricao) values(?, ?)', feriados)


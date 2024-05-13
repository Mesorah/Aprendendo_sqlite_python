import sqlite3
from contextlib import closing
from pathlib import Path

ARQUIVO_BRUTO = Path(__file__).parent
NOME_BANCO = 'brasil.db'
ARQUIVO_COMPLETO = ARQUIVO_BRUTO / NOME_BANCO

dados = [
    ["Acre", 894470],
    ["Alagoas", 3351543],
    ["Amapá", 861773],
    ["Amazonas", 4207714],
    ["Bahia", 14873064],
    ["Ceará", 9132078],
    ["Distrito Federal", 3055149],
    ["Espírito Santo", 4064052],
    ["Goiás", 7113540],
    ["Maranhão", 7075181],
    ["Mato Grosso", 3526220],
    ["Mato Grosso do Sul", 2778986],
    ["Minas Gerais", 21168791],
    ["Pará", 8690745],
    ["Paraíba", 4039277],
    ["Paraná", 11516840],
    ["Pernambuco", 9616621],
    ["Piauí", 3281480],
    ["Rio de Janeiro", 17366189],
    ["Rio Grande do Norte", 3534165],
    ["Rio Grande do Sul", 11422973],
    ["Rondônia", 1796460],
    ["Roraima", 631181],
    ["Santa Catarina", 7252502],
    ["São Paulo", 46649132],
    ["Sergipe", 2318822],
    ["Tocantins", 1590248]
]

with sqlite3.connect(ARQUIVO_COMPLETO) as connection:
    connection.row_factory = sqlite3.Row
    with closing(connection.cursor()) as cursor:
        cursor.execute("""CREATE TABLE estados(id integer primary key autoincrement,
                        nome text, populacao integer)""")
        
        cursor.executemany('INSERT INTO estados(nome, populacao) VALUES(?,?)', dados)
        
    connection.commit()
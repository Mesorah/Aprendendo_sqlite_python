import sqlite3
from contextlib import closing
from pathlib import Path

ARQUIVO_BRUTO = Path(__file__).parent
NOME_BANCO = 'meus_testes.db'
ARQUIVO_COMPLETO = ARQUIVO_BRUTO / NOME_BANCO

with sqlite3.connect(ARQUIVO_COMPLETO) as connection:
    with closing(connection.cursor()) as cursor:
        cursor.execute('CREATE TABLE IF NOT EXISTS testes(nome varchar, sobrenome varchar)')
        connection.commit()

        cursor.execute('INSERT INTO IF NOT EXISTS testes(nome, sobrenome) VALUES (?,?)', ('carlos', 'veiga'))
        connection.commit()

        cursor.execute('SELECT * FROM testes')

        resultado = cursor.fetchall()

        for valores in resultado:

            print(f'Nome: {valores[0]}\nSobrenome: {valores[1]}\n')
import sqlite3
from contextlib import closing
from pathlib import Path

ARQUIVO_BRUTO = Path(__file__).parent
NOME_BANCO = 'brasil.db'
ARQUIVO_COMPLETO = ARQUIVO_BRUTO / NOME_BANCO

dados = [
    ["AC", "n", "Acre"],
    ["AL", "ne", "Alagoas"],
    ["AP", "n", "Amapá"],
    ["AM", "n", "Amazonas"],
    ["BA", "ne", "Bahia"],
    ["CE", "ne", "Ceará"],
    ["DF", "co", "Distrito Federal"],
    ["ES", "se", "Espírito Santo"],
    ["GO", "co", "Goiás"],
    ["MA", "ne", "Maranhão"],
    ["MT", "co", "Mato Grosso"],
    ["MS", "co", "Mato Grosso do Sul"],
    ["MG", "se", "Minas Gerais"],
    ["PA", "n", "Pará"],
    ["PB", "ne", "Paraíba"],
    ["PR", "se", "Paraná"],
    ["PE", "ne", "Pernambuco"],
    ["PI", "ne", "Piauí"],
    ["RJ", "se", "Rio de Janeiro"],
    ["RN", "ne", "Rio Grande do Norte"],
    ["RS", "se", "Rio Grande do Sul"],
    ["RO", "no", "Rondônia"],
    ["RR", "n", "Roraima"],
    ["SC", "se", "Santa Catarina"],
    ["SP", "se", "São Paulo"],
    ["SE", "se", "Sergipe"],
    ["TO", "co", "Tocantins"]
]


with sqlite3.connect(ARQUIVO_COMPLETO) as connection:
    connection.executemany('UPDATE estados set sigla = ?, regiao = ? where nome = ?', dados)
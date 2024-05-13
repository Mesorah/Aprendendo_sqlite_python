import sqlite3
from contextlib import closing
from pathlib import Path

ARQUIVO_BRUTO = Path(__file__).parent
NOME_BANCO = 'brasil.db'
ARQUIVO_COMPLETO = ARQUIVO_BRUTO / NOME_BANCO

print('Região Estados População Mínima    Máxima    Média    Total (soma)')
print('===== ========           =======  ========   ======   =============')

with sqlite3.connect(ARQUIVO_COMPLETO) as connection:
    for regiao in connection.execute('''
        SELECT regiao, count(*), min(populacao), max(populacao), avg(populacao), sum(populacao) as tpop
        FROM estados GROUP BY regiao HAVING count(*) > 5 ORDER BY tpop desc
    '''):
        # Imprimir dados de cada região
        print('{0:6} {1:7} {2:18,} {3:10,} {4:10,.0f} {5:13,}'.format(*regiao))

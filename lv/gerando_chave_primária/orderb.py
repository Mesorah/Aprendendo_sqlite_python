import sqlite3
from contextlib import closing
from pathlib import Path

ARQUIVO_BRUTO = Path(__file__).parent
NOME_BANCO = 'brasil.db'
ARQUIVO_COMPLETO = ARQUIVO_BRUTO / NOME_BANCO

print('Região Estados População Mínima    Máxima    Média    Total (soma)')
print('===== ========           =======  ========   ======   =============')

with sqlite3.connect(ARQUIVO_COMPLETO) as connection:
    # Consulta para obter dados do Brasil
    dados_brasil = connection.execute('''
        SELECT count(*), min(populacao), max(populacao), avg(populacao), sum(populacao) FROM estados
    ''').fetchone()

    for regiao in connection.execute('''
        SELECT regiao, count(*), min(populacao), max(populacao), avg(populacao), sum(populacao) as tpop
        FROM estados GROUP BY regiao ORDER BY tpop desc
    '''):
        # Imprimir dados de cada região
        print('{0:6} {1:7} {2:18,} {3:10,} {4:10,.0f} {5:13,}'.format(*regiao))
    
    # Imprimir dados do Brasil
    print('\nBrasil: {0:6} {1:18,} {2:10,} {3:10,.0f} {4:13,}'.format(*dados_brasil))

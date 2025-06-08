import pandas as pd
from pandasql import sqldf



def pysqldf(q):
    return sqldf(q, globals())

df_pessoas = pd.read_excel('Pessoas.xlsx')

result = pysqldf(''' SELECT Nome, Pais, Idade FROM df_pessoas WHERE Idade > 85 ORDER BY Idade ASC ''')
print(result)
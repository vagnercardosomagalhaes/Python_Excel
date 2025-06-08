import pandas as pd

df = pd.read_excel('Origem.xlsx')
#print(df)

df['MILHAR'] = pd.Series([1000,2000,3000,4000,5000])

#print(df)

df.to_excel('destino.xlsx', sheet_name='Numeros', index=False) #copio o conteudo de origem para o arquivo destino

df2 = pd.read_excel('destino.xlsx')
print(df2)
import pandas as pd

df = pd.read_excel('Pessoas.xlsx')

columns = ['Nome', 'Pais', 'Idade']

#ukr = df[columns].where(df['Pais'] == 'Ukraine')

#ukr = ukr.dropna()# remove linhas com valores NaN

#print('\n* Ukraines') 
#print(ukr)

#velhos = df[columns].where(df['Idade'] > 85)

#velhos = velhos.dropna()
#print('\n* Velhos > 85') 
#print(velhos)

velhos = df[columns].where((df['Pais'] == 'Ukraine') & (df['Idade'] > 50))
velhosUK = velhos.dropna() 
print('\n* Velhos ucranianos > 85') 
print(velhosUK)
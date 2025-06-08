import pandas as pd

data = {
    'Unidades': pd.Series([1, 2, 3, 4, 5]),
    'Dezenas': pd.Series([10, 20, 30, 40, 50]),
    'Centenas': pd.Series([100, 200, 300, 400, 500]),
}

df = pd.DataFrame(data)

print(df)
print('')
print(df['Unidades'])
print('')
print(df[['Dezenas']])
print('')
print(df[['Unidades', 'Dezenas' ,'Centenas']])
print('')
df['Total'] = df['Unidades'] + df['Dezenas'] + df['Centenas']
print(df[['Unidades', 'Dezenas', 'Centenas', 'Total']])
del df['Total']
print(df)

df.pop('Unidades')
print(df)
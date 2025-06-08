import requests
import pandas as pd

url = 'https://jsonplaceholder.typicode.com/photos'

r = requests.get(url)
data = r.json()
#print(data)

df = pd.DataFrame(data)

print('Exportado json para xlsx')

df = df.to_excel('destino2.xlsx', index = False)

print('Exportação finalizada')

print(df)
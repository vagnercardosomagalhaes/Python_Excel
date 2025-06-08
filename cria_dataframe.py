import pandas as pd

data = [['Alex',10],['Milene', 20],['Alfredo', 30],['Rose',40],['Luana',50],['Heloisa',60]]


data2={
    'Nome': ['Alex', 'Milene', 'Alfredo', 'Rose', 'Luana', 'Heloisa'],
    'Idade': [11, 22, 33, 44, 55, 66]   
}

data3={
    'Nome': ['Alex', 'Milene', 'Alfredo', 'Rose', 'Luana', 'Heloisa'],
    'Idade': [11, 22, 33, 44, 55, 66],
    'Cidade': ['SP', 'RJ', 'MG', 'RS', 'BA', 'PE']

}


df = pd.DataFrame(data, columns=['Nome', 'Idade'])
print(df)

df = pd.DataFrame(data2)
print(df)

df = pd.DataFrame(data3, index=['a', 'b', 'c', 'd', 'e', 'f'])  
print(df)



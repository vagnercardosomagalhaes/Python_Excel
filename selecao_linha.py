import pandas as pd

d = {
        'Dezenas': pd.Series(
        [10, 20, 30, 40, 50],
        index=['a', 'b', 'c', 'd', 'e']
        ),
        'Centenas': pd.Series(
        [100, 200, 300, 400, 500],
        index=['a', 'b', 'c', 'd', 'e']
        )
    }

df = pd.DataFrame(d)

print(df)
print('------------------------------')
print(df.loc['b'])
print('------------------------------')
print(df.iloc[3])

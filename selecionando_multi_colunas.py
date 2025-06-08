import pandas as pd

d = {
        'Dezenas': pd.Series([10,20,30]),
        'Centenas': pd.Series([100,200,300])

    }
df = pd.DataFrame(d)
print(df)
print('------------------------------')

print(df[1:3]) # listando mais de uma linha, indice da primeira linha e o indice da segunda linha(+1)
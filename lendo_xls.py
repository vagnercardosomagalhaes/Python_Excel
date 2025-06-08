import pandas as pd

file_name='Pasta1.xlsx'
df = pd.read_excel(file_name)

data= {
    'UNIDADES': pd.Series([6,7,8]),
    'DEZENAS': pd.Series([60,70,80])
}

df = pd.DataFrame(data)

workbook = 'Num_DataFrame.xlsx'
sheet = 'Aba1'

df.to_excel(workbook,sheet, index=False)


#print(df)


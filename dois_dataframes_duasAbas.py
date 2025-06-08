import pandas as pd

df_unidades = pd.DataFrame({'UNIDADES': [6,7,8]})
df_dezenas =  pd.DataFrame({'DEZENAS': [60,70,80]})

with pd.ExcelWriter('UnidadesSeparadas.xlsx') as writer:

    df_unidades.to_excel(writer, sheet_name='UNIDADES', index=False)
    df_dezenas.to_excel(writer, sheet_name='DEZENAS', index=False)



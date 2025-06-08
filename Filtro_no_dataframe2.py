import pandas as pd

df = pd.read_excel('Funcionarios-Dados.xlsx')
df2 = pd.read_excel('Funcionarios-Notas.xlsx')

#df_nome_in_df2 = df[df['Nome'].isin(df2['Nome'])] # filtra nomes que estao no df e no df2 ao mesmo tempo

#print('\nNomes presentes no df e no df2\n')
#print(df_nome_in_df2)

#para listar somente quem esta em uma das planilhas

#df_nome_not_df2 = df[~df['Nome'].isin(df2['Nome'])]

#print('\nNomes presentes no df e NÂO no df2\n')
#print(df_nome_not_df2)

#para listar nomes qu estao nas duas listas e que tenham nota acima de 4

#df_nome_in_df2_and_notaUP4 = df[df['Nome'].isin(df2['Nome']) & (df['Nota Entrevista'] > 4)] 

#print('\nNomes presentes no df e no df2 e que tenha nota acima de 4\n')
#print(df_nome_in_df2_and_notaUP4)

#Juntando dois dataframes em um só, a partir de um dado comum entre os dois - nesse caso o Nome
df_marged = pd.merge(df,df2, how='outer', on='Nome')
result = df_marged.loc[(df_marged['Anos de Experiencia'] < 5) & (df_marged['Nota em Grupo'] > 4)]

print('\nUnindo as duas tabelas\n')
print(result)




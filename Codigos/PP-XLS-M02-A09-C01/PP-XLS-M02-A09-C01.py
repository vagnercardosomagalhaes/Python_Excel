# coding=utf-8
#
# Copyright © 2020 por Tiago Petrucci Ribeiro
# PRODUTIVIDADE PROGRAMADA – Ganhe tempo, escala e motivação.
# https://www.produtividadeprogramada.com.br
#
# PP-XLS-M02-A09-C01
# Leitura de dados de um arquivo .xlsx.
#
# Documentação Dataframe
# https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
#

import pandas as pd

file_name = 'Numeros.xlsx'
df = pd.read_excel(file_name)

print(df)

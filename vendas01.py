import os
from pathlib import Path
import pandas as pd

script_path = os.getcwd()  # Caminho de onde o script é executado

def get_all_files_path():
    files_path = []

    vendas_path = Path(script_path) / 'Vendas'

    for loja_dir in vendas_path.iterdir():
        if loja_dir.is_dir():
            for mes_dir in loja_dir.iterdir():
                if mes_dir.is_dir():
                    for file in mes_dir.iterdir():
                        if file.is_file() and file.suffix in ['.xlsx', '.xls']:  # Evita .DS_Store ou pastas
                            files_path.append(file)
                            print(f"Arquivo encontrado: {file}")

    return files_path


def get_sales_dataframe(files_path):
    sales_df = pd.DataFrame(columns=['Loja', 'Vendedor', 'Valor da Venda'])

    for path in files_path:
        try:
            df = pd.read_excel(path)

            # Verifica se as colunas esperadas existem
            if {'Loja', 'Vendedor', 'Valor da Venda'}.issubset(df.columns):
                sales_df = pd.concat([sales_df, df[['Loja', 'Vendedor', 'Valor da Venda']]], ignore_index=True)
            else:
                print(f"Colunas ausentes no arquivo: {path}")

        except Exception as e:
            print(f"Erro ao ler {path}: {e}")

    return sales_df


# Executando o fluxo
files_path = get_all_files_path()
sales_df = get_sales_dataframe(files_path)

# Mostrando o DataFrame final
print("\nDataFrame Consolidado:")
print(sales_df)

# Totalizador por loja
total_por_loja = sales_df.groupby('Loja')['Valor da Venda'].sum().reset_index()

# Exibindo o totalizador
print("\nTotal de vendas por loja:")
print(total_por_loja)

#gerando xlsx com total por loja
total_por_loja.to_excel('total_por_loja.xlsx', index=False)

# Totalizador por vendedor
total_por_vendedor = sales_df.groupby('Vendedor')['Valor da Venda'].sum().reset_index()

# Exibindo o totalizador
print("\nTotal de vendas por vendedor:")
print(total_por_vendedor)

#gerando xlsx com total por vendedor
total_por_vendedor.to_excel('total_por_vendedor.xlsx', index=False)


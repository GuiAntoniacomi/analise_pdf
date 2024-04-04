from tabula import read_pdf
import pandas as pd

# Caminho para o arquivo PDF
arquivo_pdf = 'src\\dificil.PDF'

# Usando tabula para ler a página do PDF que contém as tabelas
# 'pages' é o número da página
tabelas = read_pdf(arquivo_pdf, pages=1, multiple_tables=True)

# Exportando cada tabela para um arquivo Excel separado
for i, tabela in enumerate(tabelas):
    # Convertendo o DataFrame para um arquivo Excel
    tabela.to_excel(f'tabela_{i+1}.xlsx', index=False)

import warnings
import tabula
import pandas as pd
from tika import parser
import re

def extrair_informacoes_pdf(nome_arquivo):
    # Faz a extração do texto do PDF
    raw_text = parser.from_file(nome_arquivo)['content']

    # Exemplo de padrões de busca (ajuste conforme o conteúdo real do PDF)
    padrao_area_construida = r'Área do\s*Terreno:\s*([\d\.,]+)\s*m²'
    # Busca pelas informações no texto extraído
    match_area_construida = re.search(padrao_area_construida, raw_text)

    area_terreno = at
    area_construida = None
    
    if match_area_construida:
        area_construida = float(match_area_construida.group(1).replace(',', '.'))

    return area_terreno, area_construida

at = float(input('Digite a área do terreno: '))
# Nome do arquivo PDF
nome_arquivo_pdf = "src/CAM2024084848-240306165204.PDF"

# Chama a função para extrair as informações
area_terreno, area_construida = extrair_informacoes_pdf(nome_arquivo_pdf)

# Exibe os resultados
print(f"Área do Terreno: {area_terreno} m²")
print(f"Área Total Construída: {area_construida} m²")

# Suprimir os avisos
warnings.filterwarnings("ignore", category=FutureWarning)

# Lê todas as tabelas do PDF
try:
    lista_tabelas = tabula.read_pdf(nome_arquivo_pdf, pages="all")
except Exception as e:
    print("Erro ao ler as tabelas do PDF:", e)
    lista_tabelas = []

# Restaura as configurações de aviso padrão
warnings.resetwarnings()

# Pergunta ao usuário qual tabela ele deseja consultar
print("Escolha uma das opções:")
print("1. USOS PERMITIDOS HABITACIONAIS")
print("2. USOS PERMITIDOS NÃO HABITACIONAIS")
print("3. USOS PERMISSÍVEIS NÃO HABITACIONAIS")

# Solicitar ao usuário que digite o número da opção desejada
opcao = input("Digite o número da opção desejada: ")

# Verifica se o input é um número inteiro válido
if opcao.isdigit():
    opcao = int(opcao)

    # Exibe a tabela correspondente
    if 1 <= opcao <= len(lista_tabelas):
        tabela_escolhida = lista_tabelas[opcao - 1]
        print("\nTabela escolhida:")
        print(tabela_escolhida)

        # Criar listas com as informações desejadas, ignorando as linhas 0 e 1
        linhas = tabela_escolhida.values.tolist()[2:]

        # Imprimir as listas
        print("\nListas criadas:")
        for linha in linhas:
            print(linha)
    else:
        print("Opção inválida. Por favor, escolha uma opção válida (1, 2 ou 3).")
else:
    print("Por favor, insira um número inteiro válido.")

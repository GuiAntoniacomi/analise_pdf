import warnings
import tabula
import pandas as pd
from tika import parser
import re

def extrair_informacoes_pdf(nome_arquivo):
    # Faz a extração do texto do PDF
    raw_text = parser.from_file(nome_arquivo)['content']

    # Exemplo de padrões de busca (ajuste conforme o conteúdo real do PDF)
    padrao_area_terreno = r'Área do\s*Terreno:\s*([\d\.,]+)\s*m²'
    padrao_area_construida = r'Área Total\s*Construída:\s*([\d\.,]+)\s*m²'

    # Busca pelas informações no texto extraído
    match_area_terreno = re.search(padrao_area_terreno, raw_text)
    match_area_construida = re.search(padrao_area_construida, raw_text)

    area_terreno = None
    area_construida = None

    if match_area_terreno:
        area_terreno = float(match_area_terreno.group(1).replace(',', '.'))
    if match_area_construida:
        area_construida = float(match_area_construida.group(1).replace(',', '.'))

    return area_terreno, area_construida

# Nome do arquivo PDF
nome_arquivo_pdf = "D:\\Users\\eugen\\Documents\\Gui\\ESTUDOS\\Python\\analise_pdf\\src\\CAM2024084848-240306165204.pdf"

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

        # Extrair opções disponíveis dinamicamente da tabela escolhida
        try:
            opcoes_disponiveis = tabela_escolhida.dropna(subset=['USOS PERMITIDOSNÃO HABITACIONAIS'])['USOS PERMITIDOSNÃO HABITACIONAIS'].tolist()
        except KeyError:
            opcoes_disponiveis = []

        if not opcoes_disponiveis:
            print("Não foi possível extrair opções disponíveis da tabela.")
        else:
            # Exibir as opções disponíveis para o usuário escolher
            print("\nOpções disponíveis:")
            for i, opcao in enumerate(opcoes_disponiveis):
                print(f"{i+1}. {opcao}")

            # Solicitar ao usuário que escolha uma opção da tabela
            escolha_opcao = input("Escolha uma opção da tabela: ")

            # Verifica se o input é um número inteiro válido
            if escolha_opcao.isdigit():
                escolha_opcao = int(escolha_opcao) - 1
                if 0 <= escolha_opcao < len(opcoes_disponiveis):
                    opcao_escolhida = opcoes_disponiveis[escolha_opcao]
                    print(f"\nOpção escolhida: {opcao_escolhida}")

                    # Realizar cálculos com base na opção escolhida e na área do terreno
                    try:
                        coeficiente_aprov = tabela_escolhida.loc[tabela_escolhida['USOS PERMITIDOSNÃO HABITACIONAIS'] == opcao_escolhida, 'COEF.'].values[0]
                        taxa_ocupacao = tabela_escolhida.loc[tabela_escolhida['USOS PERMITIDOSNÃO HABITACIONAIS'] == opcao_escolhida, 'TAXA DE OCUPAÇÃO'].values[0]
                        ca = coeficiente_aprov * area_terreno
                        to = taxa_ocupacao * area_terreno

                        print(f"\nCoeficiente de Aproveitamento (ca): {ca} m²")
                        print(f"Taxa de Ocupação (to): {to} m²")
                    except Exception as e:
                        print("Erro ao calcular os valores:", e)
                else:
                    print("Opção inválida.")
            else:
                print("Por favor, insira um número inteiro válido.")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida (1, 2 ou 3).")
else:
    print("Por favor, insira um número inteiro válido.")

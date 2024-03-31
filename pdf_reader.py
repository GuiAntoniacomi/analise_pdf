import warnings
import tabula
import pandas as pd
import re

def extrair_opcoes_pdf(nome_arquivo):
    # Suprimir os avisos
    warnings.filterwarnings("ignore", category=FutureWarning)

    try:
        # Lê todas as tabelas do PDF
        lista_tabelas = tabula.read_pdf(nome_arquivo, pages="all")
    except Exception as e:
        print("Erro ao ler as tabelas do PDF:", e)
        lista_tabelas = []

    # Restaura as configurações de aviso padrão
    warnings.resetwarnings()

    return lista_tabelas

def converter_linha_para_dicionario(linha):
    # Converter uma linha da tabela em um dicionário
    dicionario = {
        "COD": linha["COD"],
        "USO": linha["USOS PERMITIDOSHABITACIONAIS"],
        "COEFIICIENTE DE APROVEITAMENTO": linha["COEF."],
        "ALTURA BASICA": linha["ALTURA (pavtos.)"],
        "TAXA DE OCUPAÇÃO": float(linha["TAXA DE OCUPAÇÃO"].split('%')[0]) / 100,
        "TAXA PERMEABILIDADE": float(linha["TAXA RECUO FRONTAL (m) MÍNIMO"].split('%')[0]) / 100,
        "RECUO FRONTAL": float(linha["TAXA RECUO FRONTAL (m) MÍNIMO"].split()[0].replace(',', '.'))
    }
    return dicionario

def calcular_valores(opcao_escolhida, area_terreno, area_construida):
    # Realizar cálculos com base na opção escolhida e nas áreas fornecidas
    try:
        coeficiente_aprov = tabela_escolhida.loc[tabela_escolhida['USOS PERMITIDOSNÃO HABITACIONAIS'] == opcao_escolhida, 'COEF.'].values[0]
        taxa_ocupacao = tabela_escolhida.loc[tabela_escolhida['USOS PERMITIDOSNÃO HABITACIONAIS'] == opcao_escolhida, 'TAXA DE OCUPAÇÃO'].values[0]
        ca = coeficiente_aprov * area_terreno
        to = taxa_ocupacao * area_terreno

        print(f"\nCoeficiente de Aproveitamento (ca): {ca} m²")
        print(f"Taxa de Ocupação (to): {to} m²")
    except Exception as e:
        print("Erro ao calcular os valores:", e)

# Nome do arquivo PDF
nome_arquivo_pdf = "D:\\Users\\eugen\\Documents\\Gui\\ESTUDOS\\Python\\analise_pdf\\src\\CAM2024084848-240306165204.pdf"

# Lê todas as tabelas do PDF
lista_tabelas = extrair_opcoes_pdf(nome_arquivo_pdf)

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

                    # Solicitar ao usuário que insira a área do terreno
                    area_terreno = input("Insira a área do terreno (em m²): ")

                    # Verifica se o input é um número válido
                    if area_terreno.replace('.', '', 1).isdigit():
                        area_terreno = float(area_terreno)

                        # Solicitar ao usuário que insira a área total construída
                        area_construida = input("Insira a área total construída (em m²): ")

                        # Verifica se o input é um número válido
                        if area_construida.replace('.', '', 1).isdigit():
                            area_construida = float(area_construida)

                            # Realizar cálculos com base na opção escolhida e nas áreas fornecidas
                            calcular_valores(opcao_escolhida, area_terreno, area_construida)
                        else:
                            print("Por favor, insira um número válido para a área total construída.")
                    else:
                        print("Por favor, insira um número válido para a área do terreno.")
                else:
                    print("Opção inválida.")
            else:
                print("Por favor, insira um número inteiro válido.")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida (1, 2 ou 3).")
else:
    print("Por favor, insira um número inteiro válido.")

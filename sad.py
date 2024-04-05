import re
from PyPDF2 import PdfReader
import Zoneamento  # Assumindo que este módulo contém as funções necessárias

def normalizar_codigo_zoneamento(codigo_zoneamento):
    # A função de normalização como definido anteriormente

def extrair_dados_zoneamento(pdf_path, page_number):
    # A função de extração como definido anteriormente

def buscar_dados_zoneamento(codigo_zoneamento):
    # A função de busca como definido anteriormente

def exibir_menu_e_obter_escolha(dados_zoneamento):
    # A função que exibe o menu como definido anteriormente

def exibir_detalhes_zoneamento(escolha, opcoes, dados_zoneamento):
    # A função que exibe os detalhes do zoneamento como definido anteriormente

# Caminho do seu arquivo PDF e página
pdf_path = "C:\\Users\\anton\\Downloads\\CAM2024084848-240306165204.PDF"
pagina_desejada = 1

# Extrai e normaliza o zoneamento do PDF
dados_extracao = extrair_dados_zoneamento(pdf_path, pagina_desejada)
codigo_zoneamento_bruto = dados_extracao.get('Zoneamento')
if codigo_zoneamento_bruto:
    codigo_zoneamento = normalizar_codigo_zoneamento(codigo_zoneamento_bruto)

    # Busca os dados do zoneamento normalizado
    dados_zoneamento = buscar_dados_zoneamento(codigo_zoneamento)

    if dados_zoneamento:
        while True:
            escolha, opcoes = exibir_menu_e_obter_escolha(dados_zoneamento)
            if escolha == 'sair':
                break
            exibir_detalhes_zoneamento(escolha, opcoes, dados_zoneamento)
    else:
        print(f"Não foram encontradas informações para o zoneamento: {codigo_zoneamento}")
else:
    print("Zoneamento não encontrado no PDF.")

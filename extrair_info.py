import re
from PyPDF2 import PdfReader
import Zoneamento  # Assumindo que este módulo contém as funções necessárias

def normalizar_codigo_zoneamento(codigo_zoneamento):
    # Remove o ponto e tudo após ele e converte para minúsculas
    codigo_zoneamento = re.sub(r'\..*', '', codigo_zoneamento).lower()
    # Substitui espaços e hífens por nada (remove-os)
    codigo_zoneamento = re.sub(r'[ -]', '', codigo_zoneamento)
    return codigo_zoneamento

def extrair_dados_zoneamento(pdf_path, page_number):
    reader = PdfReader(pdf_path)
    page_text = reader.pages[page_number - 1].extract_text()
    
    padrao_zoneamento = r'Zoneamento:\s*(\w+\.\d+.*?)(?=\n)'
    zoneamento_match = re.search(padrao_zoneamento, page_text)

    dados_zoneamento = {}
    if zoneamento_match:
        dados_zoneamento['Zoneamento'] = zoneamento_match.group(1)

    return dados_zoneamento

def buscar_dados_zoneamento(codigo_zoneamento):
    nome_funcao = f'get_{codigo_zoneamento}_data'
    if hasattr(Zoneamento, nome_funcao):
        get_data_func = getattr(Zoneamento, nome_funcao)
        return get_data_func()
    else:
        return None

def exibir_menu_e_obter_escolha(dados_zoneamento):
    opcoes = list(dados_zoneamento.keys())
    print("\nO que você gostaria de consultar?")
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i}. {opcao}")
    
    escolha = input("Digite o número da opção desejada ou 'sair' para terminar: ").strip().lower()
    return escolha, opcoes

def exibir_detalhes_zoneamento(escolha, opcoes, dados_zoneamento):
    if escolha.isdigit():
        escolha_index = int(escolha) - 1
        if 0 <= escolha_index < len(opcoes):
            categoria_escolhida = opcoes[escolha_index]
            detalhes = dados_zoneamento[categoria_escolhida]
            print(f"\nDetalhes para {categoria_escolhida}:")
            for uso, detalhes_uso in detalhes.items():
                print(f"\n{uso}:")
                for chave, valor in detalhes_uso.items():
                    print(f"  {chave}: {valor}")
        else:
            print("Opção inválida. Tente novamente.")
    elif escolha == 'sair':
        print("Programa encerrado.")
    else:
        print("Por favor, insira um número válido.")
# Caminho do seu arquivo PDF
pdf_path = "C:\\Users\\anton\\Downloads\\CAM2024084848-240306165204.PDF"
pagina_desejada = 1  # Ajuste para a página correta

# Supondo que 'dados_zoneamento' seja o dicionário retornado pela sua função de busca
dados_zoneamento = buscar_dados_zoneamento(codigo_zoneamento)

while True:
    escolha, opcoes = exibir_menu_e_obter_escolha(dados_zoneamento)
    if escolha == 'sair':
        break
    exibir_detalhes_zoneamento(escolha, opcoes, dados_zoneamento)

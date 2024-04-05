import re
from tika import parser

def normalizar_codigo_zoneamento(codigo):
    # Remove pontos e converte para minúsculas
    return re.sub(r'\.', '', codigo).lower()

def extrair_zoneamento(nome_arquivo):
    # Faz a extração do texto do PDF
    raw_text = parser.from_file(nome_arquivo)['content']
    
    # Exemplo de padrões de busca
    padrao_zoneamento = r'Zoneamento:\s*([A-Z]{2,3}\.\d+)'  # Ajuste conforme necessário
    # Busca pelas informações no texto extraído
    match_zoneamento = re.search(padrao_zoneamento, raw_text)
    
    zoneamento = None
    if match_zoneamento:
        zoneamento = normalizar_codigo_zoneamento(match_zoneamento.group(1))
        
    return zoneamento

# Nome do arquivo PDF
nome_arquivo_pdf = "C:\\Users\\anton\\Downloads\\CAM2024084848-240306165204.PDF"

# Chama a função para extrair o zoneamento
zoneamento = extrair_zoneamento(nome_arquivo_pdf)

# Agora vamos integrar a extração com o código de busca no banco de dados
import Zoneamento

def consultar_zoneamento(zoneamento):
    # Normaliza o código de zoneamento
    zona_normalizada = normalizar_codigo_zoneamento(zoneamento)
    
    try:
        # Tenta encontrar os dados usando o código de zoneamento normalizado
        get_data_func = getattr(Zoneamento, f'get_{zona_normalizada}_data')
        zoneamento_data = get_data_func()
        # ... (continuação do código existente para trabalhar com os dados encontrados) ...
    except AttributeError:
        print("\nZoneamento não encontrado no banco de dados. Tente novamente.")

# Chama a função de consulta com o zoneamento extraído
if zoneamento:
    consultar_zoneamento(zoneamento)
else:
    print("Não foi possível identificar o zoneamento no PDF.")

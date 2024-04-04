import re
from PyPDF2 import PdfReader

def extrair_dados_zoneamento(pdf_path, page_number):
    # Extrai texto de uma página específica
    reader = PdfReader(pdf_path)
    page_text = reader.pages[page_number - 1].extract_text()  # Ajuste o índice de página

    # Processa o texto extraído (você precisará adaptar a lógica abaixo para suas necessidades)
    linhas = page_text.split('\n')
    dados_zoneamento = {}
    for linha in linhas:
        # Substitua os seguintes padrões pela lógica específica de sua página
        if 'USOS' in linha and 'PERMITIDOS' in linha:
            categoria_atual = 'USOS PERMITIDOS'
            dados_zoneamento[categoria_atual] = {}
        elif re.match(r'algum padrão regex', linha):  # Use expressões regulares conforme necessário
            pass  # Processamento específico aqui

    # Organizar os dados estruturados
    # Você pode usar regex, split ou outras operações de string para organizar seus dados

    return dados_zoneamento

# Caminho do seu arquivo PDF
pdf_path = 'caminho/para/seu/arquivo.pdf'

# Substitua pelo número da página que você deseja processar
pagina_desejada = 64

# Chamar a função e imprimir os resultados
dados = extrair_dados_zoneamento(pdf_path, pagina_desejada)
print(dados)

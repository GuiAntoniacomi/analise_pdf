import re
from tika import parser

def corrigir_texto_extraido(texto):
    # Correção específica para a concatenação errada da "Qtde. de Sublotes" e "Área do Terreno"
    texto_corrigido = re.sub(
        pattern=r"Qtde\. de Sublotes: 1(\d{3}),00 m²",
        repl=r"Área do Terreno: \1,00 m²\nQtde. de Sublotes: 1",
        string=texto
    )
    return texto_corrigido

def extrair_areas(pdf_text):
    # Primeiro, aplicar a correção ao texto extraído
    pdf_text_corrigido = corrigir_texto_extraido(pdf_text)
    #print("Texto corrigido:")
    #print(pdf_text_corrigido)

    # Ajustando as expressões regulares com base no entendimento correto da estrutura do documento
    padrao_area_terreno = r'Área do\s*Terreno:\s*([\d\.,]+)\s*m²'
    padrao_area_construida = r'Área Total Construída:\s*([\d\.,]+)\s*m²'
    
    # Procura pelos padrões no texto corrigido
    area_terreno_match = re.search(padrao_area_terreno, pdf_text_corrigido)
    print("Match para área do terreno:")
    print(area_terreno_match)

    area_construida_match = re.search(padrao_area_construida, pdf_text_corrigido)
    print("Match para área total construída:")
    print(area_construida_match)

    # Extrai e ajusta os dados encontrados para formato numérico
    area_terreno = float(area_terreno_match.group(1).replace(',', '.')) if area_terreno_match else None
    area_construida = float(area_construida_match.group(1).replace(',', '.')) if area_construida_match else None

    return area_terreno, area_construida

# Exemplo de como você usaria a função
# Nota: Este bloco precisa ser executado no seu ambiente local, já que depende do arquivo PDF e da biblioteca tika
pdf_path = "C:\\Users\\anton\\Downloads\\zoneamento\\areas.pdf"
raw_text = parser.from_file(pdf_path)['content']
area_terreno, area_construida = extrair_areas(raw_text)
print(f"Área do Terreno: {area_terreno} m²")
print(f"Área Total Construída: {area_construida} m²")

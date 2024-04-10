from pdfquery import PDFQuery
import re

def solicitar_arquivo_pdf():
    pdf_path = input("Por favor, insira o caminho do arquivo PDF da guia amarela: ")
    return pdf_path

def buscar_info_por_texto_na_pagina(pdf, texto):
    qtde_paginas = len(pdf.pq('LTPage'))
    
    for num_pagina in range(qtde_paginas):
        # Carrega a página atual do PDF
        pdf.load(num_pagina)        
        todos_os_elementos_dessa_pagina = pdf.pq('*')
                
        bbox_esticada = []
        for elemento in todos_os_elementos_dessa_pagina:
            if elemento.text and texto in elemento.text:
                # Defina sua lógica para "esticar" a bbox baseada no texto encontrado
                bbox_esticada = definir_bbox_de_busca_por_texto(elemento)
                break
        
        if bbox_esticada:
            # Procura elementos que "encostam" na bbox esticada
            for elemento in todos_os_elementos_dessa_pagina:
                try:
                    bbox_elemento = [
                        float(elemento.get('x0')),
                        float(elemento.get('y0')),
                        float(elemento.get('x1')),
                        float(elemento.get('y1'))
                    ]
                except:
                    continue
                
                if bbox_encostando(bbox_elemento, bbox_esticada) and elemento.text:
                    if 'Área' in texto:
                        return pegar_valor_numerico_da_area(elemento)
                    elif 'Bairro' in texto:
                        return pegar_nome_do_bairro(elemento)
                    elif 'Zoneamento' in texto:
                        return pegar_codigo_zoneamento(elemento)
    return None  # Retorna None se não encontrar a informação

def extrair_informacoes_pdf(pdf_path):
    pdf = PDFQuery(pdf_path)
    pdf.load()

    info_pdf = {
        'zoneamento': buscar_info_por_texto_na_pagina(pdf, 'Zoneamento:'),
        'bairro': buscar_info_por_texto_na_pagina(pdf, 'Bairro:'),
        'area_terreno': buscar_info_por_texto_na_pagina(pdf, 'Área do Terreno:'),
        'area_construida': buscar_info_por_texto_na_pagina(pdf, 'Área Total Construída:')
    }

    return info_pdf

if __name__ == '__main__':
    pdf_path = solicitar_arquivo_pdf()
    info_pdf = extrair_informacoes_pdf(pdf_path)
    print(info_pdf)

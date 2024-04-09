from pdfquery import PDFQuery
import re
from tika import parser
import tabula
import xml.etree.ElementTree as ET

def elemento_dentro_da_bbox(element_bbox, target_bbox):
    """
    Check if the given element's bbox is within the target bbox.
    element_bbox: List of [x0, y0, x1, y1] coordinates of the element.
    target_bbox: List of [x0, y0, x1, y1] coordinates of the target bbox.
    """
    x0, y0, x1, y1 = element_bbox
    target_x0, target_y0, target_x1, target_y1 = target_bbox

    return (x0 >= target_x0 and y0 >= target_y0 and
            x1 <= target_x1 and y1 <= target_y1)

def definir_bbox_de_busca_por_texto(texto):
    # Define bbox de busca para ser a bbox do elemento do texto 'esticada' 150px na horizontal
    elementos = pdf.pq(f'LTTextLineHorizontal:contains("{texto}")')
    bbox_de_busca = []
    if elementos:
        x0 = float(elementos[0].get('x0'))
        y0 = float(elementos[0].get('y0'))
        x1 = float(elementos[0].get('x1')) + 150.0
        y1 = float(elementos[0].get('y1'))
        
        bbox_de_busca = [x0, y0, x1, y1]
    return bbox_de_busca

def definir_valor_por_texto(texto):
    bbox_de_busca = definir_bbox_de_busca_por_texto(texto)
    
    # PEga todos os elementos da página
    todos_os_elementos = pdf.pq('LTPage').find('*')

    # Separa só os elementos que estão dentro da bbox de busca
    elementos_na_bbox_de_busca = []
    for elemento in todos_os_elementos:
        bbox_desse_elemento = [
            float(elemento.get('x0')),
            float(elemento.get('y0')),
            float(elemento.get('x1')),
            float(elemento.get('y1'))
        ]

        # Verifica se o elemento ta dentro da bbox de busca
        if elemento_dentro_da_bbox(bbox_desse_elemento, bbox_de_busca):
            elementos_na_bbox_de_busca.append(elemento)
    
    if elementos_na_bbox_de_busca:        
        for elemento in elementos_na_bbox_de_busca:
            # texto_elemento é algo no formato 111,11 m²
            texto_elemento = elemento.text.strip()
            if 'm²' in texto_elemento:
                # retira o m²
                numeros_e_virgula = re.findall(r'[\d,]+', texto_elemento)

                # Cria uma string numerica no formato 111,11
                parte_numerica = ''.join(numeros_e_virgula)

                # Troca , por . pro python poder transformar string em float
                parte_numerica = float(parte_numerica.replace(',', '.')) 

                break
        return parte_numerica
    else:
        print("Elementos não encontrados na bbox de busca")
        return None

if __name__ == '__main__':    
    print("GOGOGO")
    pdf_path = 'D:/Projetos/analise_pdf/src/novo.PDF'

    # Initialize PDFQuery and load the PDF file
    pdf = PDFQuery(pdf_path)
    pdf.load()

    area_do_terreno = definir_valor_por_texto('Área do Terreno:')    
    print('Área do Terreno:',area_do_terreno)

    area_total_contruida = definir_valor_por_texto('Área Total Construída:')    
    print('Área Total Construída:',area_total_contruida)
    
        
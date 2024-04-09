from pdfquery import PDFQuery
import re

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

def obter_num_da_pagina_por_texto(pdf, texto):
    # Iterate through each page to search for the target text
    for num_pagina in range(len(pdf.pq('LTPage'))):
        pdf.load(num_pagina)
        
        todos_os_elementos_dessa_pagina = pdf.pq('LTTextLineHorizontal')
        
        # Check each text element to find the target text
        for elemento in todos_os_elementos_dessa_pagina:
            if texto in elemento.text:
                return num_pagina + 1 
                
    # Return None if the target text is not found in any page
    return None

def bbox_encostando(element_bbox, target_bbox):
    target_x0, target_y0, target_x1, target_y1 = target_bbox
    element_x0, element_y0, element_x1, element_y1 = element_bbox

    # Check for overlap in the x-axis and y-axis
    x_overlap = (element_x0 < target_x1) and (element_x1 > target_x0)
    y_overlap = (abs(element_y0 - target_y0) < 5) and (abs(element_y1 - target_y1) < 5)

    return x_overlap and y_overlap

def definir_bbox_de_busca_por_texto(elemento):
    # Define bbox de busca para ser a bbox do elemento do texto 'esticada' 150px na horizontal
    x0 = float(elemento.get('x0'))
    y0 = float(elemento.get('y0'))
    x1 = float(elemento.get('x1')) + 30.0
    y1 = float(elemento.get('y1'))
    
    bbox_de_busca = [x0, y0, x1, y1]
    return bbox_de_busca

def pegar_valor_numerico_da_area(elementos_na_bbox_de_busca):
    parte_numerica = None
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

def pegar_nome_do_bairro(elementos_encostando_em_bbox_esticada):
    # Ignora o elemento elemento que contém 'Bairro' no texto
    nome = ''
    for elemento in elementos_encostando_em_bbox_esticada:
        texto_do_elemento = elemento.text.strip()
        if 'Bairro:' not in texto_do_elemento:
            nome = texto_do_elemento
    return nome

def pegar_codigo_zoneamento(elementos_encostando_em_bbox_esticada):
    # o texto do único elemento de zoneamento tem formato 'Zoneamento: ZR3.1 - ZONA RESIDENCIAL 3 '
    info = elementos_encostando_em_bbox_esticada[0].text.strip()

    # Transforma em lista ['Zoneamento', 'ZR3.1', '-', 'ZONA', 'RESIDENCIAL', '3']
    infos_em_lista = info.split(' ')

    # Separa o código em infos_em_lista[1] para ['ZR3', '.'] e pega o primeiro elemento
    codigo = infos_em_lista[1].split('.')[0]
    return codigo

def buscar_info_por_texto_na_pagina(texto):
    pdf = PDFQuery(PDF_PATH)
    pdf.load()    
    qtde_paginas = len(pdf.pq('LTPage'))
    
    for num_pagina in range(qtde_paginas):
        # Procura o texto desejado em cada página do pdf
        pdf.load(num_pagina)        
        todos_os_elementos_dessa_pagina = pdf.pq('*')
                
        bbox_esticada = []
        for elemento in todos_os_elementos_dessa_pagina:
            if elemento.text and texto in elemento.text:
                # Caso o texto seja encontrado em algum elemento da página, salva a bbox esticada
                bbox_esticada = definir_bbox_de_busca_por_texto(elemento)
                break
        
        elementos_encostando_em_bbox_esticada = []
        if bbox_esticada:
            # Caso alguma bbox_esticada tenha sido salva, procura todos os elementos que encostam na bbox esticada
            for elemento in todos_os_elementos_dessa_pagina:
                try:
                    bbox_desse_elemento = [
                        float(elemento.get('x0')),
                        float(elemento.get('y0')),
                        float(elemento.get('x1')),
                        float(elemento.get('y1'))
                    ]
                except:
                    continue
                if bbox_encostando(bbox_desse_elemento, bbox_esticada) and elemento.text:
                    elementos_encostando_em_bbox_esticada.append(elemento) 
        
        if elementos_encostando_em_bbox_esticada:        
            # Caso exista algum elemento nessa página encostando na bbox esticada, pega o valor desejado
            # Cada tipo de busca trata os resultados de maneira diferente
            if 'Área' in texto:
                resultado = pegar_valor_numerico_da_area(elementos_encostando_em_bbox_esticada)
            elif 'Bairro' in texto:
                resultado = pegar_nome_do_bairro(elementos_encostando_em_bbox_esticada)
            elif 'Zoneamento' in texto:
                resultado = pegar_codigo_zoneamento(elementos_encostando_em_bbox_esticada)
            
            return resultado
        
        

if __name__ == '__main__':    
    print("GOGOGO")
    PDF_PATH = 'D:/Projetos/analise_pdf/src/CAM2024084848-240306165204.PDF'

    info_pdf = {
        'zoneamento': buscar_info_por_texto_na_pagina('Zoneamento:'),
        'bairro': buscar_info_por_texto_na_pagina('Bairro:'),
        'area_terreno': buscar_info_por_texto_na_pagina('Área do Terreno:'),
        'area_construida': buscar_info_por_texto_na_pagina('Área Total Construída:')   
    }

    print(info_pdf)
import PyPDF2
import re
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def extract_info(pdf_path):
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = reader.getPage(0).extractText()

    # Extrair informações específicas usando expressões regulares
    area = re.findall(r'Área do Terreno:\s+(\d+)', text)[0]
    coeficiente = re.findall(r'Coeficiente de Aproveitamento:\s+(\d+)', text)[0]

    # Salvar as informações em um dicionário
    info = {
        'area': area,
        'coeficiente': coeficiente,
    }

    return info

def main():
    # Extrair informações da guia amarela
    info = extract_info("D:\\Users\\eugen\\Documents\\Gui\\ESTUDOS\\Python\\analise_pdf\\src\\CAM2024084848-240306165204.pdf")

    # Abrir o site e preencher o campo
    webbrowser.open('https://geocuritiba.ippuc.org.br/mapacadastral/')
    time.sleep(3)  # Espera 3 segundos para garantir que a página seja carregada completamente

    # Simular cliques e digitações com Selenium
    driver = webdriver.Chrome()  # Abre o navegador Chrome
    driver.get('https://geocuritiba.ippuc.org.br/mapacadastral/')
    time.sleep(3)  # Espera 3 segundos para garantir que a página seja carregada completamente

    # Encontra o campo de pesquisa e preenche com a área extraída
    campo_pesquisa = driver.find_element_by_id('Area')
    campo_pesquisa.send_keys(info['area'])
    campo_pesquisa.send_keys(Keys.RETURN)

if __name__ == '__main__':
    main()

from pdf2image import convert_from_path
from pytesseract import image_to_string
import re
from PIL import Image

def pdf_to_img(pdf_path):
    return convert_from_path(pdf_path)

def ocr_from_image(images):
    for image in images:
        text = image_to_string(image)

        # Regex patterns for the target information
        area_terreno_pattern = r'Área do Terreno:?\s*(\d{1,3}(?:\.\d{3})*,\d{2})\s*m²'
        area_construida_pattern = r'Área Total Construída:?\s*(\d{1,3}(?:\.\d{3})*,\d{2})\s*m²'
        qtde_sublotes_pattern = r'Qtde\.? de Sublotes:?\s*(\d+)'

        # Extracting information using the regex patterns
        area_terreno_match = re.search(area_terreno_pattern, text)
        area_construida_match = re.search(area_construida_pattern, text)
        qtde_sublotes_match = re.search(qtde_sublotes_pattern, text)

        # Parsing the matches to the appropriate data type
        area_terreno = area_terreno_match.group(1).replace('.', '').replace(',', '.') if area_terreno_match else None
        area_construida = area_construida_match.group(1).replace('.', '').replace(',', '.') if area_construida_match else None
        qtde_sublotes = int(qtde_sublotes_match.group(1)) if qtde_sublotes_match else None

        if area_terreno or area_construida or qtde_sublotes:
            return {
                'Área do Terreno': area_terreno,
                'Área Total Construída': area_construida,
                'Quantidade de Sublotes': qtde_sublotes
            }
    return None

# Replace with the actual path to your PDF file
pdf_path = r"src\\CAM2024084848-240306165204.PDF"
images = pdf_to_img(pdf_path)
extracted_info = ocr_from_image(images)
print(extracted_info)

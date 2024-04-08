from pytesseract import image_to_string
from PIL import Image
import re

def extract_info_from_image(image_path):
    # Open the image file
    img = Image.open(image_path)
    # Use pytesseract to do OCR on the image
    text = image_to_string(img)

    # Adjusted regex patterns for more flexibility
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

    return {
        'Área do Terreno': area_terreno,
        'Área Total Construída': area_construida,
        'Quantidade de Sublotes': qtde_sublotes
    }

# Usage example - this needs to be run in your local environment
image_path = "C:\\Users\\anton\\Downloads\\zoneamento\\areas.jpg"  # Replace with the actual path to your image file
extracted_info = extract_info_from_image(image_path)
print(extracted_info)

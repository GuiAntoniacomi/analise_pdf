import tabula

# Lê todas as tabelas do PDF
lista_tabelas = tabula.read_pdf("D:\\Users\\eugen\\Documents\\Gui\\ESTUDOS\\Python\\analise_pdf\\src\\CAM2024084848-240306165204.pdf", pages="all")

# Exibe o número de tabelas encontradas
print(f"Encontradas {len(lista_tabelas)} tabelas.")

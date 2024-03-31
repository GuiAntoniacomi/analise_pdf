import warnings
import tabula
from tika import parser

def extrair_informacoes_pdf(nome_arquivo):
    # Faz a extração do texto do PDF
    raw_text = parser.from_file(nome_arquivo)['content']

    # Inicializa a lista de permitidos_habitacionais
    permitidos_habitacionais = []

    # Extrai as linhas da tabela
    linhas = raw_text.split('\n')

    # Pula as primeiras linhas até encontrar o cabeçalho da tabela
    i = 0
    while i < len(linhas) and 'USOS PERMITIDOSHABITACIONAIS' not in linhas[i]:
        i += 1

    # Avança mais uma linha para pular o cabeçalho
    i += 1

    # Itera sobre as linhas restantes da tabela
    while i < len(linhas) and linhas[i]:
        # Divide a linha em campos usando espaço como separador
        campos = linhas[i].split()

        # Verifica se a linha possui o número correto de campos
        if len(campos) >= 6:
            # Verifica se o campo pode ser convertido para inteiro
            try:
                coeficiente_aprov = int(campos[1])
            except ValueError:
                coeficiente_aprov = 0

            # Converte os outros valores necessários para os tipos corretos
            uso = campos[0]
            altura = int(campos[2])
            permeabilidade = int(campos[3])
            recuo_frontal = float(campos[4].replace(',', '.'))
            taxa_ocupacao = int(campos[5])

            # Adiciona os valores na lista permitidos_habitacionais
            permitidos_habitacionais.append([uso, coeficiente_aprov, altura, permeabilidade, recuo_frontal, taxa_ocupacao])

        # Avança para a próxima linha
        i += 1

    return permitidos_habitacionais


# Nome do arquivo PDF (ajuste conforme o nome real)
nome_arquivo_pdf = "D:\\Users\\eugen\\Documents\\Gui\\ESTUDOS\\Python\\analise_pdf\\src\\CAM2024084848-240306165204.pdf"

# Chama a função para extrair as informações
permitidos_habitacionais = extrair_informacoes_pdf(nome_arquivo_pdf)

# Exibe os resultados
print("Tabela de Usos Permitidos Habitacionais:")
for item in permitidos_habitacionais:
    print(item)


import warnings
import tabula
import pandas as pd
import re

def encontrar_opcoes_disponiveis(lista_tabelas):
    opcoes_disponiveis = []

    for tabela in lista_tabelas:
        # Procura por uma correspondência parcial usando expressões regulares
        matches = tabela.columns.str.contains(r'USOS\s*PERMITIDOS\s*HABITACIONAIS', flags=re.IGNORECASE)
        if any(matches):
            opcoes_disponiveis.append("USOS PERMITIDOS HABITACIONAIS")
        else:
            matches = tabela.columns.str.contains(r'USOS\s*PERMITIDOS\s*NÃO\s*HABITACIONAIS', flags=re.IGNORECASE)
            if any(matches):
                opcoes_disponiveis.append("USOS PERMITIDOS NÃO HABITACIONAIS")
            else:
                matches = tabela.columns.str.contains(r'USOS\s*PERMISSÍVEIS\s*NÃO\s*HABITACIONAIS', flags=re.IGNORECASE)
                if any(matches):
                    opcoes_disponiveis.append("USOS PERMISSÍVEIS NÃO HABITACIONAIS")
                else:
                    matches = tabela.columns.str.contains(r'USOS\s*PERMISSÍVEIS\s*HABITACIONAIS', flags=re.IGNORECASE)
                    if any(matches):
                      opcoes_disponiveis.append("USOS PERMISSÍVEIS HABITACIONAIS")
    return opcoes_disponiveis

# Suprimir os avisos
warnings.filterwarnings("ignore", category=FutureWarning)

# Lê todas as tabelas do PDF
lista_tabelas = tabula.read_pdf("src\\novo.PDF", pages="1")

# Restaura as configurações de aviso padrão
warnings.resetwarnings()

# Lê todas as tabelas do PDF
try:
    lista_tabelas
except Exception as e:
    print("Erro ao ler as tabelas do PDF:", e)
    lista_tabelas = []

# Encontra as opções disponíveis
opcoes_disponiveis = encontrar_opcoes_disponiveis(lista_tabelas)

# Exibir as opções disponíveis para o usuário escolher
print("\nOpções disponíveis:")
for i, opcao in enumerate(opcoes_disponiveis):
    print(f"{i+1}. {opcao}")

opcao = int(input("Digite o número da opção desejada: "))

# Exibe a tabela correspondente
if 1 <= opcao <= len(lista_tabelas):
    tabela_escolhida = lista_tabelas[opcao - 1]
    print("\nTabela escolhida:")
    print(tabela_escolhida)

# Criar listas com as informações desejadas, ignorando as linhas 0 e 1
linhas = tabela_escolhida.values.tolist()[2:]

# Criar um dicionário para mapear nomes de habitação para seus índices
habitacao_indices = {linha[0]: i for i, linha in enumerate(linhas)}

# Display numbered habitation type options
print("\nOpções de Habitação:")
for i, tipo_habitacao in enumerate(habitacao_indices.keys()):
        print(f"{i+1}. {tipo_habitacao}")

# Prompt user to choose habitation type by number
while True:
    try:
        opcao_habitacao = int(input("Digite o número da opção desejada: "))
        if 1 <= opcao_habitacao <= len(habitacao_indices):
            break
        else:
            print("Opção inválida. Por favor, digite um número entre 1 e", len(habitacao_indices))
    except ValueError:
        print("Valor inválido. Digite um número inteiro.")

# Get the chosen habitation type and its index
tipo_habitacao_escolhido = list(habitacao_indices.keys())[opcao_habitacao - 1]
indice_habitacao_escolhido = habitacao_indices[tipo_habitacao_escolhido]

# Calcular área máxima construtível para cada tipo de habitação
for linha in linhas:
    if linha[0] != "USOS PERMITIDOS NÃO HABITACIONAIS":  # Ignorar linha de cabeçalho
        tipo_habitacao = linha[0]  # Extrair tipo de habitação
        coef_utilizacao = linha[1] if pd.notna(linha[1]) else None  # Coeficiente de aproveitamento

        # Converter o coeficiente para um número de ponto flutuante, se não for NaN
        if coef_utilizacao is not None and isinstance(coef_utilizacao, str):
            try:
                coef_utilizacao = float(coef_utilizacao.replace(",", "."))  # Substituir ',' por '.' se presente
            except ValueError:
                coef_utilizacao = None

        # Se o coeficiente ainda não estiver disponível, solicitar ao usuário que o insira manualmente
        if coef_utilizacao is None:
            print('Parece que estamos com dificuldades para ler esse PDF.')
            coef_utilizacao = float(input('Digite o coeficiente de aproveitamento: '))

        # Solicitar ao usuário a área do terreno e converter para float
        area_terreno = float(input(f"Digite a área do terreno para {tipo_habitacao} (em metros quadrados): "))

        # Calcular área máxima construtível
        if coef_utilizacao is not None:
            area_maxima_construtivel = area_terreno * coef_utilizacao
            print(f"Tipo de Habitação: {tipo_habitacao}")
            print(f"Coef. Aproveitamento: {coef_utilizacao}")
            print(f"Área Máxima Construtível: {area_maxima_construtivel:.2f} m²")
            print("-" * 30)  # Separador entre tipos de habitação
            break
        else:
            print(f"Erro ao calcular Área Máxima Construtível para {tipo_habitacao} - Coeficiente de Aproveitamento indisponível.")
            print("-" * 30)  # Separador entre tipos de habitação
            break

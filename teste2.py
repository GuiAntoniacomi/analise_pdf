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
lista_tabelas = tabula.read_pdf("src\\CAM2024084848-240306165204.PDF", pages="1")

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
    #print("\nTabela escolhida:")
    #print(tabela_escolhida)

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

def converter_para_numero(valor):
    if pd.notna(valor):
        if isinstance(valor, str):
            try:
                return float(valor.replace(",", "."))
            except ValueError:
                return None
        elif isinstance(valor, (int, float)):
            return valor
    return None

# Calcular área máxima construtível para cada tipo de habitação
# Calcular área máxima construtível para cada tipo de habitação
for linha in linhas:
    if linha[0] != "USOS PERMITIDOS NÃO HABITACIONAIS":  # Ignorar linha de cabeçalho
        tipo_habitacao = linha[0]  # Extrair tipo de habitação
        coef_utilizacao = converter_para_numero(linha[1])  # Coeficiente de aproveitamento
        taxa_ocupacao = converter_para_numero(linha[4])  # Taxa de ocupação permitida
        altura_permitida = converter_para_numero(linha[2])  # Altura permitida

        # Se o coeficiente ainda não estiver disponível, solicitar ao usuário que o insira manualmente
        if coef_utilizacao is None:
            print('Parece que estamos com dificuldades para ler esse PDF.')
            coef_utilizacao = float(input('Digite o coeficiente de aproveitamento: '))

        # Solicitar ao usuário a área do terreno e converter para float
        area_terreno = float(input(f"Digite a área do terreno para {tipo_habitacao} (em metros quadrados): "))

        # Inicializar área máxima construtível
        area_maxima_construtivel = area_terreno * coef_utilizacao

        # Determinar se há uma edificação construída
        tem_edificacao_construida = input("Existe alguma edificação construída no terreno? (S/N): ").upper() == "S"
        if tem_edificacao_construida:
            manter_edificacao = input("Você pretende manter essa edificação? (S/N): ").upper() == "S"
            if manter_edificacao:
                area_construida_atual = float(input("Digite a área construída atualmente (em metros quadrados): "))
                area_maxima_construtivel -= area_construida_atual

        # Calcular área máxima construtível
        if coef_utilizacao is not None:
            taxa_ocupacao_final = area_terreno * (taxa_ocupacao / 100) if taxa_ocupacao is not None else None
            num_pav = area_maxima_construtivel / taxa_ocupacao_final if taxa_ocupacao_final != 0 else None

            print(f"Tipo de Habitação: {tipo_habitacao}")
            print(f"Coef. Aproveitamento: {coef_utilizacao}")
            print(f"Taxa de Ocupação Permitida: {taxa_ocupacao}%")
            if taxa_ocupacao_final is not None:
                print(f"Taxa de Ocupação Calculada: {taxa_ocupacao_final:.2f} m²")
                if altura_permitida is not None:
                    if num_pav is not None and num_pav <= altura_permitida:
                        print(f'É possível comprar potencial construtivo e adicionar {altura_permitida - num_pav:.0f} pavimentos.')
                    else:
                        print(f'O máximo de pavimentos permitidos por lei é {altura_permitida}.')
            else:
                print("Erro ao calcular Taxa de Ocupação - Valor indisponível.")
            print(f"Área Máxima Construtível: {area_maxima_construtivel:.2f} m²")
            print("-" * 30)  # Separador entre tipos de habitação
        else:
            print(f"Erro ao calcular Área Máxima Construtível para {tipo_habitacao} - Coeficiente de Aproveitamento indisponível.")
            print("-" * 30)  # Separador entre tipos de habitação
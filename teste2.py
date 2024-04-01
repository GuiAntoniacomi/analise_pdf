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
    lista_tabelas = tabula.read_pdf('src\\CAM2024084848-240306165204.PDF', pages="all")
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

    # Imprimir as listas
    print("\nListas criadas:")
    for linha in linhas:
        print(linha)
else:
    print("Opção inválida. Por favor, escolha uma opção válida (1, 2 ou 3).")


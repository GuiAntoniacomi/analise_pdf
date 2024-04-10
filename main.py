import re
from tika import parser
import Zoneamento  # Este módulo contém as funções necessárias como get_zfr_data()

from extracao_pdf.extrair_info import extrair_info_completa

def normalizar_codigo_zoneamento(codigo_zoneamento):
    return re.sub(r'\.\d+.*', '', codigo_zoneamento).lower()

def buscar_dados_zoneamento(codigo_zoneamento):
    codigo_zoneamento = normalizar_codigo_zoneamento(codigo_zoneamento)
    nome_funcao = f'get_{codigo_zoneamento}_data'
    if hasattr(Zoneamento, nome_funcao):
        get_data_func = getattr(Zoneamento, nome_funcao)
        return get_data_func()
    else:
        return None

def exibir_categorias_e_obter_escolha(dados_zoneamento):
    opcoes = list(dados_zoneamento.keys())
    print("\nCategorias disponíveis:")
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i}. {opcao}")
    escolha = input("Escolha uma categoria (número) ou digite 'sair' para terminar: ").strip().lower()
    if escolha.isdigit() and 0 < int(escolha) <= len(opcoes):
        return opcoes[int(escolha) - 1], opcoes
    elif escolha == 'sair':
        return 'sair', opcoes
    else:
        print("Opção inválida.")
        return None, opcoes

def exibir_usos_e_obter_escolha(categoria, dados_zoneamento):
    usos = list(dados_zoneamento[categoria].keys())
    print(f"\nUsos disponíveis em {categoria}:")
    for i, uso in enumerate(usos, start=1):
        print(f"{i}. {uso}")
    escolha_uso = input("Escolha um uso (número) ou digite 'voltar' para escolher outra categoria: ").strip().lower()
    if escolha_uso.isdigit() and 0 < int(escolha_uso) <= len(usos):
        return usos[int(escolha_uso) - 1]
    elif escolha_uso == 'voltar':
        return 'voltar'
    else:
        print("Opção inválida.")
        return None

def exibir_detalhes_uso(categoria, uso_escolhido, dados_zoneamento):
    detalhes = dados_zoneamento[categoria].get(uso_escolhido, {})
    print(f"\nDetalhes para {uso_escolhido} em {categoria}:")
    for chave, valor in detalhes.items():
        if isinstance(valor, list):
            for item in valor:
                print(f"  - {item}")
        else:
            print(f"  {chave}: {valor}")

def main():
    pdf_path = input("Por favor, insira o caminho do arquivo PDF da guia amarela: ")
    info_pdf = extrair_info_completa(pdf_path)
    codigo_zoneamento_bruto = info_pdf.get('zoneamento')

    if codigo_zoneamento_bruto:
        codigo_zoneamento = normalizar_codigo_zoneamento(codigo_zoneamento_bruto)
        dados_zoneamento = buscar_dados_zoneamento(codigo_zoneamento)
        
        if dados_zoneamento:
            while True:
                categoria_selecionada, categorias = exibir_categorias_e_obter_escolha(dados_zoneamento)
                if categoria_selecionada == 'sair':
                    break
                elif categoria_selecionada:
                    uso_selecionado = exibir_usos_e_obter_escolha(categoria_selecionada, dados_zoneamento)
                    if uso_selecionado == 'voltar':
                        continue
                    elif uso_selecionado:
                        exibir_detalhes_uso(categoria_selecionada, uso_selecionado, dados_zoneamento)
                else:
                    continue  # Se opção inválida, volta ao início do loop
        else:
            print(f"Não foram encontradas informações para o zoneamento: {codigo_zoneamento}")
    else:
        print("Zoneamento não encontrado no PDF.")

if __name__ == "__main__":
    main()

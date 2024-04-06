import re
from PyPDF2 import PdfReader
from tika import parser
import Zoneamento  # Este módulo deve conter as funções necessárias como get_zfr_data()

def normalizar_codigo_zoneamento(codigo_zoneamento):
    return re.sub(r'\.\d+.*', '', codigo_zoneamento).lower()

def extrair_dados_zoneamento(pdf_path, page_number):
    raw_text = parser.from_file(pdf_path)['content']
    padrao_zoneamento = r'Zoneamento:\s*([A-Z]{2,3}\.\d+)'
    match_zoneamento = re.search(padrao_zoneamento, raw_text)
    if match_zoneamento:
        return {'Zoneamento': match_zoneamento.group(1)}
    else:
        return {'Zoneamento': None}

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
    escolha = input("Escolha uma categoria ou digite 'sair' para terminar: ").strip().lower()
    return escolha, opcoes

def exibir_usos_e_obter_escolha(categoria, dados_zoneamento):
    if categoria in dados_zoneamento:
        usos = list(dados_zoneamento[categoria].keys())
        print(f"\nUsos disponíveis em {categoria}:")
        for i, uso in enumerate(usos, start=1):
            print(f"{i}. {uso}")
        escolha_uso = input("Escolha um uso para ver detalhes ou digite 'voltar' para escolher outra categoria: ").strip().lower()
        return escolha_uso, usos
    else:
        print("Categoria não encontrada.")
        return None, None

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
    pdf_path = "src\\CAM2024084848-240306165204.PDF"
    pagina_desejada = 1
    dados_extracao = extrair_dados_zoneamento(pdf_path, pagina_desejada)
    codigo_zoneamento_bruto = dados_extracao.get('Zoneamento')

    if codigo_zoneamento_bruto:
        codigo_zoneamento = normalizar_codigo_zoneamento(codigo_zoneamento_bruto)
        dados_zoneamento = buscar_dados_zoneamento(codigo_zoneamento)
        if dados_zoneamento:
            while True:
                escolha_categoria, categorias = exibir_categorias_e_obter_escolha(dados_zoneamento)
                if escolha_categoria.lower() == 'sair':
                    break
                elif escolha_categoria.isdigit() and 0 < int(escolha_categoria) <= len(categorias):
                    categoria_selecionada = categorias[int(escolha_categoria) - 1]
                    escolha_uso, usos = exibir_usos_e_obter_escolha(categoria_selecionada, dados_zoneamento)
                    if escolha_uso == 'voltar':
                        continue
                    elif escolha_uso.isdigit() and 0 < int(escolha_uso) <= len(usos):
                        uso_selecionado = usos[int(escolha_uso) - 1]
                        exibir_detalhes_uso(categoria_selecionada, uso_selecionado, dados_zoneamento)
                    else:
                        print("Opção inválida.")
                else:
                    print("Opção inválida.")
        else:
            print(f"Não foram encontradas informações para o zoneamento: {codigo_zoneamento}")
    else:
        print("Zoneamento não encontrado no PDF.")

if __name__ == "__main__":
    main()

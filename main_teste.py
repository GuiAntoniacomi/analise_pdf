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
    # A função precisa retornar dois valores (uso_selecionado e usos) em todas as rotas de saída
    usos = dados_zoneamento[categoria].keys() if categoria in dados_zoneamento else []
    print(f"\nUsos disponíveis em {categoria}:")
    for i, uso in enumerate(usos, start=1):
        print(f"{i}. {uso}")
    escolha_uso = input("Escolha um uso (número) ou digite 'voltar' para escolher outra categoria: ").strip().lower()

    if escolha_uso.isdigit() and 0 < int(escolha_uso) <= len(usos):
        return list(usos)[int(escolha_uso) - 1], list(usos)
    elif escolha_uso == 'voltar':
        return 'voltar', list(usos)

    return None, list(usos)

def exibir_detalhes_uso(categoria, uso_escolhido, dados_zoneamento):
    detalhes = dados_zoneamento[categoria].get(uso_escolhido, {})
    print(f"\nDetalhes para {uso_escolhido} em {categoria}:")
    for chave, valor in detalhes.items():
        if isinstance(valor, list):
            for item in valor:
                print(f"  - {item}")
        else:
            print(f"  {chave}: {valor}")

def calcular_e_exibir_informacoes_importantes(area_terreno, detalhes_uso):
    print(f"O lote tem {area_terreno} m²")

    coeficiente_aproveitamento = detalhes_uso.get('COEFICIENTE DE APROVEITAMENTO')
    taxa_ocupacao_maxima = detalhes_uso.get('TAXA DE OCUPAÇÃO MÁXIMA')
    altura_basica = detalhes_uso.get('ALTURA (pavimentos)')

    if coeficiente_aproveitamento and taxa_ocupacao_maxima and altura_basica:
        area_maxima_construcao = area_terreno * coeficiente_aproveitamento
        area_por_pavimento = area_terreno * taxa_ocupacao_maxima
        numero_pavimentos_calculados = area_maxima_construcao / area_por_pavimento
        
        print(f"Com base no coeficiente de aproveitamento, você pode construir até {area_maxima_construcao:.2f} m².")
        
        if numero_pavimentos_calculados > altura_basica:
            print(f"Calculamos que você pode construir {numero_pavimentos_calculados:.2f} pavimentos, entretanto o zoneamento permite a construção de {altura_basica} pavimentos, então você pode:")
            area_por_pavimento_altura_basica = (area_terreno * coeficiente_aproveitamento) / altura_basica
            print(f"1. Dividir sua taxa de ocupação e construir {altura_basica} pavimentos de {area_por_pavimento_altura_basica:.2f} m² cada.")
            print(f"2. Comprar potencial construtivo e adicionar {altura_basica - numero_pavimentos_calculados:.2f} pavimentos adicionais ao seu projeto.")
        elif numero_pavimentos_calculados <= altura_basica:
            print(f"A quantidade de pavimentos permitida é {altura_basica}, veja a possibilidade de vender potencial construtivo.")
    else:
        if not coeficiente_aproveitamento:
            print("Coeficiente de aproveitamento não encontrado.")
        if not taxa_ocupacao_maxima:
            print("Taxa de ocupação máxima não encontrada.")
        if not altura_basica:
            print("Altura básica não encontrada.")


def main():
    pdf_path = input("Por favor, insira o caminho do arquivo PDF da guia amarela: ")
    info_pdf = extrair_info_completa(pdf_path)

    print(f"\nO zoneamento no seu lote é {info_pdf.get('zoneamento')}.")

    area_terreno = info_pdf.get('area_terreno')  # Assegure-se de que a chave corresponde à extração
    codigo_zoneamento_bruto = info_pdf.get('zoneamento')

    if codigo_zoneamento_bruto:
        codigo_zoneamento = normalizar_codigo_zoneamento(codigo_zoneamento_bruto)
        dados_zoneamento = buscar_dados_zoneamento(codigo_zoneamento)
        
        if dados_zoneamento:
            categoria_selecionada, _ = exibir_categorias_e_obter_escolha(dados_zoneamento)
            if categoria_selecionada and categoria_selecionada != 'sair':
                uso_selecionado, _ = exibir_usos_e_obter_escolha(categoria_selecionada, dados_zoneamento)
                if uso_selecionado and uso_selecionado != 'voltar':
                    detalhes_uso = dados_zoneamento[categoria_selecionada].get(uso_selecionado)
                    if detalhes_uso:  # Verifica se encontrou detalhes para o uso selecionado
                        calcular_e_exibir_informacoes_importantes(area_terreno, detalhes_uso)
                    else:
                        print("Detalhes do uso selecionado não encontrados.")
                else:
                    print("Nenhum uso foi selecionado ou o usuário optou por voltar.")
            else:
                print("Nenhuma categoria foi selecionada ou o usuário optou por sair.")
        else:
            print(f"Não foram encontradas informações para o zoneamento: {codigo_zoneamento}")
    else:
        print("Zoneamento não encontrado no PDF.")

if __name__ == "__main__":
    main()

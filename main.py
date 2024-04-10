import re
from tika import parser
import Zoneamento

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
    if categoria in dados_zoneamento:
        usos = list(dados_zoneamento[categoria].keys())
        print(f"\nUsos disponíveis em {categoria}:")
        for i, uso in enumerate(usos, start=1):
            print(f"{i}. {uso}")
        escolha_uso = input("Escolha um uso (número) ou digite 'voltar' para escolher outra categoria: ").strip().lower()
        
        if escolha_uso == 'voltar':
            return 'voltar', usos
        elif escolha_uso.isdigit() and 0 < int(escolha_uso) <= len(usos):
            return usos[int(escolha_uso) - 1], usos
    else:
        print("Categoria não encontrada.")

    return None, None  # Se nenhuma opção válida foi selecionada ou a categoria não foi encontrada

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
    
    if coeficiente_aproveitamento and taxa_ocupacao_maxima:
        area_maxima_construcao = area_terreno * coeficiente_aproveitamento
        print(f"Você pode construir até {area_maxima_construcao:.2f} m² de acordo com o coeficiente de aproveitamento do zoneamento.")
        
        # Calculando a área que pode ser construída por pavimento
        area_por_pavimento = area_terreno * taxa_ocupacao_maxima
        print(f"Por pavimento, você pode construir {area_por_pavimento:.2f} m².")
        
        # Calculando o número de pavimentos possíveis
        if area_por_pavimento > 0:  # Evita divisão por zero
            numero_pavimentos = area_maxima_construcao / area_por_pavimento
            print(f"Assim, você pode construir uma edificação de {numero_pavimentos:.2f} pavimentos de {area_por_pavimento:.2f} m² cada.")
        else:
            print("A taxa de ocupação máxima precisa ser maior que 0 para calcular o número de pavimentos.")
    else:
        if not coeficiente_aproveitamento:
            print("Coeficiente de aproveitamento não encontrado.")
        if not taxa_ocupacao_maxima:
            print("Taxa de ocupação máxima não encontrada.")

def main():
    pdf_path = input("Por favor, insira o caminho do arquivo PDF da guia amarela: ")
    info_pdf = extrair_info_completa(pdf_path)

    area_terreno = info_pdf.get('area_terreno')  # Certifique-se de que esta chave corresponde à extração
    codigo_zoneamento_bruto = info_pdf.get('zoneamento')

    if codigo_zoneamento_bruto:
        codigo_zoneamento = normalizar_codigo_zoneamento(codigo_zoneamento_bruto)
        print(f"O zoneamento no seu lote é {codigo_zoneamento_bruto}.")
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


import Zoneamento

def get_usos_disponiveis(dados_zoneamento):
    usos = []
    for categoria in dados_zoneamento.values():
        if isinstance(categoria, dict):
            usos.extend(categoria.keys())
    return usos

def main():
    while True:
        zoneamento_escolhido = input("\nDigite o nome do zoneamento (ex: 'zr1', 'zr2') ou 'sair' para terminar: ")
        if zoneamento_escolhido.lower() == 'sair':
            break
        
        try:
            get_data_func = getattr(Zoneamento, f'get_{zoneamento_escolhido.lower()}_data')
            zoneamento_data = get_data_func()
            
            usos_disponiveis = get_usos_disponiveis(zoneamento_data)
            if not usos_disponiveis:
                print("\nNenhum uso disponível encontrado para este zoneamento.")
                continue
            
            print(f"\nUsos disponíveis para {zoneamento_escolhido.upper()}:")
            for index, uso in enumerate(usos_disponiveis, start=1):
                print(f"{index}. {uso}")
            
            escolha_usuario = input("\nEscolha uma opção (número) para ver detalhes ou 'voltar' para escolher outro zoneamento: ")
            if escolha_usuario.lower() == 'voltar':
                continue
            
            try:
                escolha_index = int(escolha_usuario) - 1
                uso_escolhido = usos_disponiveis[escolha_index]
            except (ValueError, IndexError):
                print("\nOpção inválida. Tente novamente.")
                continue

            for categoria, usos in zoneamento_data.items():
                if uso_escolhido in usos:
                    detalhes_do_uso = usos[uso_escolhido]
                    print(f"\nDetalhes para {uso_escolhido}:")
                    for chave, valor in detalhes_do_uso.items():
                        print(f"{chave}: {valor}")
                    break
            else:
                print("\nUso não encontrado.")
                
        except AttributeError:
            print("\nZoneamento não encontrado. Tente novamente.")

if __name__ == "__main__":
    main()

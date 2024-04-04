# Com base nas informações extraídas, vamos criar um dicionário para a Zona de Uso Misto 1 - ZUM-1

# Estrutura de dicionário para ZUM-1
zoneamento_zum1 = {
    'Habitação Unifamiliar': {
        'COEFICIENTE DE APROVEITAMENTO': 'Básico',
        'ALTURA': 'Básico',  # Até 2 pavimentos é facultado
        'PORTE': 'Básico',
        'TAXA DE OCUPAÇÃO': 50,
        'RECUO': 5,
        'TAXA DE PERMEABILIDADE': 25,
        'AFASTAMENTO DAS DIVISAS': None,  # O documento não especifica um valor mínimo
        'LOTE PADRÃO': '15x450'
    },
    'Habitação Unifamiliar em série': {
        'COEFICIENTE DE APROVEITAMENTO': 1,
        'ALTURA': 4,  # Até 2 pavimentos é facultado, acima disso a altura é H/6
        'PORTE': None,  # O documento não especifica um valor
        'TAXA DE OCUPAÇÃO': 50,
        'RECUO': 5,
        'TAXA DE PERMEABILIDADE': 25,
        'AFASTAMENTO DAS DIVISAS': None,  # O documento não especifica um valor mínimo
        'LOTE PADRÃO': None  # O documento não especifica um padrão
    },
    'Habitação Coletiva': {
        'COEFICIENTE DE APROVEITAMENTO': 1,
        'ALTURA': 4,  # Regras similares à habitação unifamiliar em série
        # Demais parâmetros a serem preenchidos conforme disponibilidade
    },
    'Habitação Institucional': {
        # Parâmetros a serem preenchidos conforme disponibilidade
    },
    'Habitação Transitória 1': {
        # Parâmetros a serem preenchidos conforme disponibilidade
    },
    'Comunitário 1 e 2': {
        # Parâmetros a serem preenchidos conforme disponibilidade
    },
    'Comércio e Serviço Vicinal de Bairro e Setorial': {
        'COEFICIENTE DE APROVEITAMENTO': 1,
        'ALTURA': 4,  # Especificações de altura seguem regras semelhantes
        'PORTE': None,  # O documento não especifica um valor
        'TAXA DE OCUPAÇÃO': 50,
        'RECUO': 5,
        'TAXA DE PERMEABILIDADE': 25,
        'AFASTAMENTO DAS DIVISAS': None,  # O documento não especifica um valor mínimo
        'LOTE PADRÃO': None  # O documento não especifica um padrão
    },
    'Posto de Abastecimento': {
        # Parâmetros a serem preenchidos conforme disponibilidade
    },
    'Comunitário 3': {
        # Parâmetros a serem preenchidos conforme disponibilidade
    },
    'Indústria Tipo 1': {
        'COEFICIENTE DE APROVEITAMENTO': None,
        'ALTURA': None,
        'PORTE': 400,
        'TAXA DE OCUPAÇÃO': None,
        'RECUO': None,
        'TAXA DE PERMEABILIDADE': None,
        'AFASTAMENTO DAS DIVISAS': None,
        'LOTE PADRÃO': None
    }
}

# Vamos imprimir a estrutura de dicionário criada para verificar
zoneamento_zum1

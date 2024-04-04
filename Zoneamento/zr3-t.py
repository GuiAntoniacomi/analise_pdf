# Com base nas informações extraídas, vamos criar um dicionário para a Zona Residencial 3 Transição - ZR3-T

# Estrutura de dicionário para ZR3-T
zoneamento_zr3t = {
    'Habitações Unifamiliares': {
        'COEFICIENTE DE APROVEITAMENTO': 'Básico',
        'ALTURA': 'Básico',  # Adicionalmente, é permitido até 3 habitações unifamiliares por lote.
        'PORTE': 'Básico',
        'TAXA DE OCUPAÇÃO': 50,
        'RECUO': 5,
        'TAXA DE PERMEABILIDADE': 25,
        'AFASTAMENTO DAS DIVISAS': None,  # O documento não especifica um valor mínimo
        'LOTE PADRÃO': '15x450'
    },
    'Habitação Coletiva': {
        'COEFICIENTE DE APROVEITAMENTO': 1,
        'ALTURA': 4,  # Em terrenos com certas testadas, é permitido até 6 pavimentos.
        # Demais parâmetros a serem preenchidos conforme disponibilidade
    },
    'Habitação Institucional': {
        # Parâmetros a serem preenchidos conforme disponibilidade
    },
    'Habitação Transitória 1': {
        # Parâmetros a serem preenchidos conforme disponibilidade
    },
    'Comunitário 1': {
        # Parâmetros a serem preenchidos conforme disponibilidade
    },
    'Edifício de escritórios e Sede Administrativa': {
        # Parâmetros a serem preenchidos conforme disponibilidade
    },
    'Comércio e Serviço Vicinal e de Bairro': {
        'COEFICIENTE DE APROVEITAMENTO': 1,
        'ALTURA': 2,
        'PORTE': 200,
        'TAXA DE OCUPAÇÃO': 50,
        'RECUO': 5,
        'TAXA DE PERMEABILIDADE': 25,
        'AFASTAMENTO DAS DIVISAS': None,
        'LOTE PADRÃO': None  # O documento não especifica um padrão
    },
    'Comunitário 2 - Culto Religioso e Saúde': {
        # Parâmetros a serem preenchidos conforme disponibilidade
    },
    'Comunitário 2 - Ensino': {
        # Parâmetros a serem preenchidos conforme disponibilidade
    },
    'Indústria do Tipo 1': {
        'COEFICIENTE DE APROVEITAMENTO': None,
        'ALTURA': None,
        'PORTE': 200,
        'TAXA DE OCUPAÇÃO': None,
        'RECUO': None,
        'TAXA DE PERMEABILIDADE': None,
        'AFASTAMENTO DAS DIVISAS': None,
        'LOTE PADRÃO': None
    }
}

# Vamos imprimir a estrutura de dicionário criada para verificar
zoneamento_zr3t

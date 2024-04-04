# Com base nas informações extraídas, vamos criar um dicionário para a Zona Residencial 4 - ZR4

# Estrutura de dicionário para ZR4
zoneamento_zr4 = {
    'Habitações Unifamiliares': {
        'COEFICIENTE DE APROVEITAMENTO': 'Básico',
        'ALTURA': 'Básico',
        'PORTE': 'Básico',
        'TAXA DE OCUPAÇÃO': 50,
        'RECUO': 5,
        'TAXA DE PERMEABILIDADE': 25,
        'AFASTAMENTO DAS DIVISAS': None,  # O documento não especifica um valor mínimo
        'LOTE PADRÃO': None  # O documento não especifica um padrão
    },
    'Habitação Unifamiliar em Série': {
        'COEFICIENTE DE APROVEITAMENTO': 1,
        'ALTURA': 2,
        'PORTE': None,  # O documento não especifica um valor
        'TAXA DE OCUPAÇÃO': 50,
        'RECUO': 5,
        'TAXA DE PERMEABILIDADE': 25,
        'AFASTAMENTO DAS DIVISAS': None,  # O documento não especifica um valor mínimo
        'LOTE PADRÃO': None  # O documento não especifica um padrão
    },
    'Habitação Coletiva': {
        # Parâmetros a serem preenchidos conforme disponibilidade
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
    'Comunitário 2 - Saúde': {
        'COEFICIENTE DE APROVEITAMENTO': None,
        'ALTURA': 2,
        'PORTE': 200,
        'TAXA DE OCUPAÇÃO': 50,
        'RECUO': 5,
        'TAXA DE PERMEABILIDADE': 25,
        'AFASTAMENTO DAS DIVISAS': None,  # O documento não especifica um valor mínimo
        'LOTE PADRÃO': None  # O documento não especifica um padrão
    },
    'Comércio e Serviço Vicinal e de Bairro': {
        # Parâmetros a serem preenchidos conforme disponibilidade
    },
    'Comunitário 2 - Culto Religioso': {
        # Parâmetros a serem preenchidos conforme disponibilidade
    },
    'Sede Administrativa': {
        # Parâmetros a serem preenchidos conforme disponibilidade
    },
    'Indústria Tipo 1': {
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
zoneamento_zr4

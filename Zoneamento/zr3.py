# Com base nas informações extraídas, vamos criar um dicionário para a Zona Residencial 3 - ZR3

# Estrutura de dicionário para ZR3
zr3 = {
    'Habitação Unifamiliar': {
        'COEFICIENTE DE APROVEITAMENTO': 'Básico',
        'ALTURA': 'Básico',
        'PORTE': 'Básico',
        'TAXA DE OCUPAÇÃO MÁXIMA': None,
        'RECUO MÍNIMO': 5,
        'TAXA DE PERMEABILIDADE MÍNIMA': 25,
        'AFASTAMENTO DAS DIVISAS MÍNIMO': None,
        'LOTE PADRÃO': '12x360'
    },
    'Habitação Unifamiliar em Série': {
        'COEFICIENTE DE APROVEITAMENTO': 1,
        'ALTURA': 3,
        'PORTE': None,
        'TAXA DE OCUPAÇÃO': 50,
        'RECUO': 5,
        'TAXA DE PERMEABILIDADE': 25,
        'AFASTAMENTO DAS DIVISAS': None,
        'LOTE PADRÃO': None
    },
    'Habitação Coletiva': {
        'COEFICIENTE DE APROVEITAMENTO': None,
        'ALTURA': None,
        # Outros parâmetros a serem preenchidos conforme disponibilidade
    },
    'Habitação Institucional': {
        # Parâmetros a serem preenchidos conforme disponibilidade
    },
    'Habitação Transitória 1': {
        'COEFICIENTE DE APROVEITAMENTO': None,
        'ALTURA': None,
        'PORTE': None,
        'TAXA DE OCUPAÇÃO': None,
        'RECUO': None,
        'TAXA DE PERMEABILIDADE': None,
        'AFASTAMENTO DAS DIVISAS': None,
        'LOTE PADRÃO': None
    },
    'Empreendimento inclusivo de habitação de interesse social': {
        # Parâmetros a serem preenchidos conforme disponibilidade
    },
    'Comunitário 1': {
        # Parâmetros a serem preenchidos conforme disponibilidade
    },
    'Comunitário 2 - Saúde': {
        # Parâmetros a serem preenchidos conforme disponibilidade
    },
    'Comércio e Serviço Vicinal e de Bairro': {
        # Parâmetros a serem preenchidos conforme disponibilidade
    },
    'Comunitário 2 - Culto Religioso': {
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
zoneamento_zr3

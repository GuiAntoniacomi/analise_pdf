zr4 = {
    'Usos Permitidos Habitacionais': {
        'Habitações Unifamiliares': {
            'COEFICIENTE DE APROVEITAMENTO': 'Básico',
            'ALTURA (pavimentos)': 2,
            'PORTE (m²)': 'Básico',
            'TAXA DE OCUPAÇÃO MÁXIMA': 50,
            'RECUO (m)': 5,
            'TAXA DE PERMEABILIDADE MÍNIMA': 25,
            'AFASTAMENTO DAS DIVISAS (m)': 'Facultado até 2 pavimentos, acima de 2 pav. = H/6 contado a partir do térreo atendido o mínimo de 2,50 m',
            'LOTE PADRÃO (testada x área)': '15x450',
            'OBSERVACOES': [
                "Deverá ser obedecida a fração de terreno de no mínimo 120 m² por unidade habitacional."
            ]
        },
        'Habitação Unifamiliar em Série': {
            # Repetir estrutura com valores específicos e observações conforme necessário
        },
        'Habitação Coletiva': {
            # Repetir estrutura com valores específicos e observações conforme necessário
        },
        # Continuar para outros usos permitidos habitacionais...
    },
    'Usos Não Habitacionais': {
        'Comércio e Serviço Vicinal e de Bairro': {
            'COEFICIENTE DE APROVEITAMENTO': 1,
            'ALTURA (pavimentos)': 2,
            'PORTE (m²)': 'Básico',
            'TAXA DE OCUPAÇÃO MÁXIMA': 50,
            'RECUO (m)': 5,
            'TAXA DE PERMEABILIDADE MÍNIMA': 25,
            'AFASTAMENTO DAS DIVISAS (m)': None,
            'LOTE PADRÃO (testada x área)': None,
            'OBSERVACOES': [
                "A critério do CMU poderá ser concedido alvará de localização para comércio e serviço vicinal ou de bairro comunitário 1 e comunitário 2 - saúde em edificação existente e porte superior a 200 m² até o máximo de 400 m²."
            ]
        },
        'Indústria do Tipo 1': {
            'COEFICIENTE DE APROVEITAMENTO': None,
            'ALTURA (pavimentos)': None,
            'PORTE (m²)': 200,
            'TAXA DE OCUPAÇÃO MÁXIMA': None,
            'RECUO (m)': None,
            'TAXA DE PERMEABILIDADE MÍNIMA': None,
            'AFASTAMENTO DAS DIVISAS (m)': None,
            'LOTE PADRÃO (testada x área)': None,
            'OBSERVACOES': [
                "Somente alvará de licença para localização em edificação existente."
            ]
        },
        # Continuar para outros usos não habitacionais...
    },
    # Incluir 'Usos Permissíveis Habitacionais' e 'Usos Permissíveis Não Habitacionais' se aplicável...
}

def get_zr4_data():
    return zr4

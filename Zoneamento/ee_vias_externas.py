ee_vias_externas = {
    'Usos Permitidos Habitacionais': {
        'Habitação Unifamiliar': {
            'COEFICIENTE DE APROVEITAMENTO': 'Básico',
            'ALTURA (pavimentos)': 2,
            'PORTE (m²)': 'Básico',
            'TAXA DE OCUPAÇÃO MÁXIMA': 0.5,
            'RECUO (m)': 10,
            'TAXA DE PERMEABILIDADE MÍNIMA': 0.25,
            'OBSERVACOES': [
                "Uma habitação unifamiliar por lote.",
                "Atender regulamentação específica."
            ]
        },
        'Habitação Coletiva': {
            # Preencher com os detalhes específicos
        },
        'Habitação Institucional': {
            # Preencher com os detalhes específicos
        },
        'Habitação Transitória 1': {
            # Preencher com os detalhes específicos
        },
        # Incluir outros usos permitidos habitacionais conforme necessário
    },
    'Usos Não Habitacionais': {
        'Comércio e Serviço Vicinal de Bairro e Setorial': {
            # Preencher com os detalhes específicos
        },
        'Comunitário 1 e 2': {
            # Preencher com os detalhes específicos
        },
        'Posto de Abastecimento': {
            # Preencher com os detalhes específicos
        },
        'Edifício Garagem': {
            # Preencher com os detalhes específicos
        },
        'Comunitário 3': {
            # Preencher com os detalhes específicos
        },
        'Indústria do Tipo 1': {
            'COEFICIENTE DE APROVEITAMENTO': None,
            'ALTURA (pavimentos)': None,
            'PORTE (m²)': 200,
            'OBSERVACOES': [
                "Somente alvará de localização em edificação existente."
            ]
        },
        # Incluir outros usos não habitacionais conforme necessário
    },
    'Usos Permissíveis Habitacionais': {
        # Preencher se houver usos permissíveis habitacionais
    },
    'Usos Permissíveis Não Habitacionais': {
        # Preencher se houver usos permissíveis não habitacionais
    }
}

def get_ee_vias_externas_data():
    return ee_vias_externas

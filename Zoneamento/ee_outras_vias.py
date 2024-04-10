ee_outras_vias = {
    'Usos Permitidos Habitacionais': {
        'Habitação Unifamiliar': {
            'COEFICIENTE DE APROVEITAMENTO': 'Básico',
            'ALTURA (pavimentos)': 'Básico',
            'PORTE (m²)': 'Básico',
            'TAXA DE OCUPAÇÃO MÁXIMA': 50,
            'RECUO (m)': 5,
            'TAXA DE PERMEABILIDADE MÍNIMA': 25,
            'AFASTAMENTO DAS DIVISAS MÍNIMO (m)': None,
            'LOTE PADRÃO (testada x área)': None,
            'OBSERVACOES': [
                "Uma habitação unifamiliar por lote.",
                "Atender regulamentação específica."
            ]
        },
        'Habitação Coletiva': {
            # Completar com os detalhes específicos
        },
        'Habitação Institucional': {
            # Completar com os detalhes específicos
        },
        'Habitação Transitória 1': {
            # Completar com os detalhes específicos
        },
        'Comunitário 1 e 2': {
            # Completar com os detalhes específicos
        },
        # Outros usos permitidos habitacionais...
    },
    'Usos Não Habitacionais': {
        'Comércio e Serviço Vicinal de Bairro e Setorial': {
            # Completar com os detalhes específicos
        },
        'Edifício Garagem': {
            # Completar com os detalhes específicos
        },
        'Posto de Abastecimento': {
            # Completar com os detalhes específicos
        },
        'Comunitário 3': {
            # Completar com os detalhes específicos
        },
        'Indústria do Tipo 1': {
            'COEFICIENTE DE APROVEITAMENTO': None,
            'ALTURA (pavimentos)': None,
            'PORTE (m²)': 200,
            'TAXA DE OCUPAÇÃO MÁXIMA': None,
            'RECUO (m)': None,
            'TAXA DE PERMEABILIDADE MÍNIMA': None,
            'AFASTAMENTO DAS DIVISAS MÍNIMO (m)': None,
            'LOTE PADRÃO (testada x área)': None,
            'OBSERVACOES': [
                "Somente alvará de localização em edificação existente."
            ]
        },
        # Outros usos não habitacionais...
    },
    'Usos Permissíveis Habitacionais': {
        # Detalhes se houver usos permissíveis habitacionais...
    },
    'Usos Permissíveis Não Habitacionais': {
        # Detalhes se houver usos permissíveis não habitacionais...
    }
}

def get_ee_outras_vias_data():
    return ee_outras_vias

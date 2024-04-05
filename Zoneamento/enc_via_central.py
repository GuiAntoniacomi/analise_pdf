enc_via_central_e_outras_vias = {
    'Usos Permitidos Habitacionais': {
        'Habitação Unifamiliar': {
            'COEFICIENTE DE APROVEITAMENTO': 'Básico',
            'ALTURA (pavimentos)': 2,
            'PORTE (m²)': 'Básico',
            'TAXA DE OCUPAÇÃO MÁXIMA': 50,
            'RECUO (m)': 10,
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
        'Comércio e Serviço Vicinal de Bairro e Setorial': {
            # Completar com os detalhes específicos
        },
        'Comunitário 1 e 2': {
            # Completar com os detalhes específicos
        },
        # Outros usos permitidos habitacionais...
    },
    'Usos Não Habitacionais': {
        'Posto de Abastecimento': {
            # Completar com os detalhes específicos
        },
        'Edifício Garagem': {
            # Completar com os detalhes específicos
        },
        'Comunitário 3': {
            # Completar com os detalhes específicos
        },
        'Indústria do Tipo 1': {
            'COEFICIENTE DE APROVEITAMENTO': None,
            'ALTURA (pavimentos)': None,
            'PORTE (m²)': 200,
            'OBSERVACOES': [
                "Somente alvará de localização em edificação existente."
            ]
        },
        # Outros usos não habitacionais...
    },
    'Usos Permissíveis': {
        # Detalhes se houver usos permissíveis...
    }
}

def get_enc_via_central_e_outras_vias_data():
    return enc_via_central_e_outras_vias

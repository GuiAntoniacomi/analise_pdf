zr1 = {
    'Usos Habitacionais Permitidos': {
        'Habitações Unifamiliares': {
            'COEFICIENTE DE APROVEITAMENTO': 1,
            'ALTURA (pavimentos)': 2,
            'PORTE (m²)': None,
            'TAXA DE OCUPAÇÃO MÁXIMA': 0.5,
            'RECUO (m)': 5,
            'TAXA DE PERMEABILIDADE MÍNIMA': 0.25,
            'AFASTAMENTO DAS DIVISAS MÍNIMO (m)': None,
            'LOTE PADRÃO (testada x área)': '15x600',
            'OBSERVACOES': [
                "limite de uma habitação unifamiliar por fração de terreno de 300 m²",
                'Taxa de permeabilidade: Atender regulação específica.'
            ]
        },
        'Habitação Unifamiliar em Série': {
            'COEFICIENTE DE APROVEITAMENTO': 1,
            'ALTURA (pavimentos)': 2,
            'PORTE (m²)': None,
            'TAXA DE OCUPAÇÃO MÁXIMA': 0.5,
            'RECUO (m)': 5,
            'TAXA DE PERMEABILIDADE MÍNIMA': 0.25,
            'AFASTAMENTO DAS DIVISAS MÍNIMO (m)': None,
            'LOTE PADRÃO (testada x área)': '15x600',
            'OBSERVACOES': [
                "Somente em terrenos com dimensões inferiores a 20.000 m2",
                'Taxa de permeabilidade: Atender regulação específica.'
            ]
        }
    },
    'Usos Não Habitacionais Permitidos': {
        'Comércio e Serviço Vicinal': {
            'COEFICIENTE DE APROVEITAMENTO': None,
            'ALTURA (pavimentos)': None,
            'PORTE (m²)': 100,
            'TAXA DE OCUPAÇÃO MÁXIMA': None,
            'RECUO (m)': None,
            'TAXA DE PERMEABILIDADE MÍNIMA': None,
            'AFASTAMENTO DAS DIVISAS MÍNIMO (m)': None,
            'LOTE PADRÃO (testada x área)': '15x600',
            'OBSERVACOES': ["Somente alvará de localização em edificação existente."]
        },
        'Indústria Tipo 1': {
            'COEFICIENTE DE APROVEITAMENTO': None,
            'ALTURA (pavimentos)': None,
            'PORTE (m²)': 100,
            'TAXA DE OCUPAÇÃO MÁXIMA': None,
            'RECUO (m)': None,
            'TAXA DE PERMEABILIDADE MÍNIMA': None,
            'AFASTAMENTO DAS DIVISAS MÍNIMO (m)': None,
            'LOTE PADRÃO (testada x área)': '15x600',
            'OBSERVACOES': ["Somente alvará de localização em edificação existente vinculada ao uso habitacional."]
        },
        # Outros usos não habitacionais...
    },
    'Usos Habitacionais Permissiveis': None,
    'Usos Não Habitacionais Permissiveis': None
}

def get_zr1_data():
    return zr1
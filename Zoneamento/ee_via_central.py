ee_via_central = {
    'Usos Habitacionais Permitidos': {
        'Habitação Unifamiliar': {
            'COEFICIENTE DE APROVEITAMENTO': 1,
            'ALTURA (pavimentos)': 2,
            'PORTE (m²)': None,
            'TAXA DE OCUPAÇÃO MÁXIMA': 0.5,
            'RECUO (m)': 10,
            'TAXA DE PERMEABILIDADE MÍNIMA': 0.25,
            'AFASTAMENTO DAS DIVISAS (m)': None,
            'LOTE PADRÃO (testada x área)': "15x450",
            'OBSERVACOES': [
                "Uma habitação unifamiliar por lote.",
                "Atender regulamentação específica.",
                "Para edificação de uma habitação unifamiliar e/ou um comércio vicinal até 200 m2 sem implantação do Plano Massa, a edificação deverá atender no quadro acima."
            ]
        },
        'Habitação Coletiva': {
            'COEFICIENTE DE APROVEITAMENTO': 4,
            'ALTURA (pavimentos)': "livre",
            'PORTE (m²)': None,
            'TAXA DE OCUPAÇÃO MÁXIMA': [
                {'pavimentos': ['Térreo', '2º'], 'taxa': 1.0},
                {'pavimentos': ['Demais'], 'taxa': 0.5}  
            ],
            'RECUO (m)': None,
            'TAXA DE PERMEABILIDADE MÍNIMA': None,
            'AFASTAMENTO DAS DIVISAS (m)': [
            {
                'parte': 'Embasamento comercial',
                'condicao': 'Atender o Plano Massa'
            },
            {
                'parte': 'Demais pavimentos',
                'regra': 'H/6, contado do embasamento',
                'minimo': 2.5
            }
            ],
            'LOTE PADRÃO (testada x área)': "15x450",
            'OBSERVACOES': [
                "Deverá ser implantado o Plano Massa conforme regulamentação específica.",
                "Nos terrenos situados no Eixo Estrutural Norte entre as Ruas dos Funcionários, Mal. Mascarenhas de Moraes, João Gbur e Mariano Gardolinski, e no Eixo Estrutural Sul entre as Ruas Pres. Kennedy, Orlando Padilha dos Santos até o cruzamento da Av. Winston Churchill com a Rua André Ferreira Barbosa, será limitado a 3 (três) o coeficiente de aproveitamento para o uso exclusivamente habitacional.",
                "Para as edificações de uso misto o coeficiente será igual a 4 (quatro).",
                "Taxa de Ocupação: Nos terrenos onde houver limitação de altura da edificação, em função do Cone da Aeronáutica, com subutilização do potencial, poderá, a critério do Conselho Municipal do Urbanismo - CMU, ser ampliada a taxa de ocupação, respeitados os afastamentos mínimos das divisas",
                "Taxa de permeabilidade: Atender regulamentação específica."
            ]
    },
       'Habitação Institucional': {
            'COEFICIENTE DE APROVEITAMENTO': 4,
            'ALTURA (pavimentos)': "livre",
            'PORTE (m²)': None,
            'TAXA DE OCUPAÇÃO MÁXIMA': [
                {'pavimentos': ['Térreo', '2º'], 'taxa': 1.0},
                {'pavimentos': ['Demais'], 'taxa': 0.5} 
            ],
            'RECUO (m)': None,
            'TAXA DE PERMEABILIDADE MÍNIMA': None,
            'AFASTAMENTO DAS DIVISAS (m)': [
            {
                'parte': 'Embasamento comercial',
                'condicao': 'Atender o Plano Massa'
            },
            {
                'parte': 'Demais pavimentos',
                'regra': 'H/6, contado do embasamento',
                'minimo': 2.5
            }
            ],
            'LOTE PADRÃO (testada x área)': "15x450",
            'OBSERVACOES': [
                "Deverá ser implantado o Plano Massa conforme regulamentação específica.",
                "Nos terrenos situados no Eixo Estrutural Norte entre as Ruas dos Funcionários, Mal. Mascarenhas de Moraes, João Gbur e Mariano Gardolinski, e no Eixo Estrutural Sul entre as Ruas Pres. Kennedy, Orlando Padilha dos Santos até o cruzamento da Av. Winston Churchill com a Rua André Ferreira Barbosa, será limitado a 3 (três) o coeficiente de aproveitamento para o uso exclusivamente habitacional.",
                "Para as edificações de uso misto o coeficiente será igual a 4 (quatro).",
                "Taxa de Ocupação: Nos terrenos onde houver limitação de altura da edificação, em função do Cone da Aeronáutica, com subutilização do potencial, poderá, a critério do Conselho Municipal do Urbanismo - CMU, ser ampliada a taxa de ocupação, respeitados os afastamentos mínimos das divisas",
                "Taxa de permeabilidade: Atender regulamentação específica."
            ]
    },
           'Habitação Transitória 1': {
            'COEFICIENTE DE APROVEITAMENTO': 4,
            'ALTURA (pavimentos)': "livre",
            'PORTE (m²)': None,
            'TAXA DE OCUPAÇÃO MÁXIMA': [
                {'pavimentos': ['Térreo', '2º'], 'taxa': 1.0},  
                {'pavimentos': ['Demais'], 'taxa': 0.5}  
            ],
            'RECUO (m)': None,
            'TAXA DE PERMEABILIDADE MÍNIMA': None,
            'AFASTAMENTO DAS DIVISAS (m)': [
            {
                'parte': 'Embasamento comercial',
                'condicao': 'Atender o Plano Massa'
            },
            {
                'parte': 'Demais pavimentos',
                'regra': 'H/6, contado do embasamento',
                'minimo': 2.5
            }
            ],
            'LOTE PADRÃO (testada x área)': "15x450",
            'OBSERVACOES': [
                "Deverá ser implantado o Plano Massa conforme regulamentação específica.",
                "Nos terrenos situados no Eixo Estrutural Norte entre as Ruas dos Funcionários, Mal. Mascarenhas de Moraes, João Gbur e Mariano Gardolinski, e no Eixo Estrutural Sul entre as Ruas Pres. Kennedy, Orlando Padilha dos Santos até o cruzamento da Av. Winston Churchill com a Rua André Ferreira Barbosa, será limitado a 3 (três) o coeficiente de aproveitamento para o uso exclusivamente habitacional.",
                "Para as edificações de uso misto o coeficiente será igual a 4 (quatro).",
                "Taxa de Ocupação: Nos terrenos onde houver limitação de altura da edificação, em função do Cone da Aeronáutica, com subutilização do potencial, poderá, a critério do Conselho Municipal do Urbanismo - CMU, ser ampliada a taxa de ocupação, respeitados os afastamentos mínimos das divisas",
                "Taxa de permeabilidade: Atender regulamentação específica."
            ]
    },
    },
    'Usos Não Habitacionais Permitidos': {
        'Comércio e Serviço Vicinal': {
            'COEFICIENTE DE APROVEITAMENTO': None,
            'ALTURA (pavimentos)': 2,
            'PORTE (m²)': 200,
            'TAXA DE OCUPAÇÃO MÁXIMA': 0.5,
            'RECUO (m)': 10,
            'TAXA DE PERMEABILIDADE MÍNIMA': 0.25,
            'AFASTAMENTO DAS DIVISAS (m)': None,
            'LOTE PADRÃO (testada x área)': "15x450",
            'OBSERVACOES': [
                "Taxa de Permeabilidade: Atender regulamentação específica.",
                "Para edificação de uma habitação unifamiliar e/ou um comércio vicinal até 200 m2 sem implantação do Plano Massa, a edificação deverá atender no quadro acima."
            ]
        },
            'Comunitário 1 e 2': {
                    'COEFICIENTE DE APROVEITAMENTO': 4,
                'ALTURA (pavimentos)': "livre",
                'PORTE (m²)': None,
                'TAXA DE OCUPAÇÃO MÁXIMA': [
                    {'pavimentos': ['Térreo', '2º'], 'taxa': 1.0},  
                    {'pavimentos': ['Demais'], 'taxa': 0.5}  
                ],
                'RECUO (m)': None,
                'TAXA DE PERMEABILIDADE MÍNIMA': None,
                'AFASTAMENTO DAS DIVISAS (m)': [
                {
                    'parte': 'Embasamento comercial',
                    'condicao': 'Atender o Plano Massa'
                },
                {
                    'parte': 'Demais pavimentos',
                    'regra': 'H/6, contado do embasamento',
                    'minimo': 2.5
                }
                ],
                'LOTE PADRÃO (testada x área)': "15x450",
                'OBSERVACOES': [
                    "Deverá ser implantado o Plano Massa conforme regulamentação específica.",
                    "Nos terrenos situados no Eixo Estrutural Norte entre as Ruas dos Funcionários, Mal. Mascarenhas de Moraes, João Gbur e Mariano Gardolinski, e no Eixo Estrutural Sul entre as Ruas Pres. Kennedy, Orlando Padilha dos Santos até o cruzamento da Av. Winston Churchill com a Rua André Ferreira Barbosa, será limitado a 3 (três) o coeficiente de aproveitamento para o uso exclusivamente habitacional.",
                    "Para as edificações de uso misto o coeficiente será igual a 4 (quatro).",
                    "Taxa de Ocupação: Nos terrenos onde houver limitação de altura da edificação, em função do Cone da Aeronáutica, com subutilização do potencial, poderá, a critério do Conselho Municipal do Urbanismo - CMU, ser ampliada a taxa de ocupação, respeitados os afastamentos mínimos das divisas",
                    "Taxa de permeabilidade: Atender regulamentação específica."
                ]
            },
            'Comércio e Serviço Vicinal de Bairro e Setorial': {
                'COEFICIENTE DE APROVEITAMENTO': 4,
                'ALTURA (pavimentos)': "livre",
                'PORTE (m²)': None,
                'TAXA DE OCUPAÇÃO MÁXIMA': [
                    {'pavimentos': ['Térreo', '2º'], 'taxa': 1.0},  
                    {'pavimentos': ['Demais'], 'taxa': 0.5}  
                ],
                'RECUO (m)': None,
                'TAXA DE PERMEABILIDADE MÍNIMA': None,
                'AFASTAMENTO DAS DIVISAS (m)': [
                {
                    'parte': 'Embasamento comercial',
                    'condicao': 'Atender o Plano Massa'
                },
                {
                    'parte': 'Demais pavimentos',
                    'regra': 'H/6, contado do embasamento',
                    'minimo': 2.5
                }
                ],
                'LOTE PADRÃO (testada x área)': "15x450",
                'OBSERVACOES': [
                    "Deverá ser implantado o Plano Massa conforme regulamentação específica.",
                    "Nos terrenos situados no Eixo Estrutural Norte entre as Ruas dos Funcionários, Mal. Mascarenhas de Moraes, João Gbur e Mariano Gardolinski, e no Eixo Estrutural Sul entre as Ruas Pres. Kennedy, Orlando Padilha dos Santos até o cruzamento da Av. Winston Churchill com a Rua André Ferreira Barbosa, será limitado a 3 (três) o coeficiente de aproveitamento para o uso exclusivamente habitacional.",
                    "Para as edificações de uso misto o coeficiente será igual a 4 (quatro).",
                    "Taxa de Ocupação: Nos terrenos onde houver limitação de altura da edificação, em função do Cone da Aeronáutica, com subutilização do potencial, poderá, a critério do Conselho Municipal do Urbanismo - CMU, ser ampliada a taxa de ocupação, respeitados os afastamentos mínimos das divisas",
                    "Taxa de permeabilidade: Atender regulamentação específica."
                ]
            },
            # Adicionar mais usos não habitacionais conforme necessário...
    },
    'Usos Habitacionais Permissíveis': None,
    'Usos Não Habitacionais Permissíveis': {
        'Comunitário': {
            'COEFICIENTE DE APROVEITAMENTO': 4,
            'ALTURA (pavimentos)': "livre",
            'PORTE (m²)': None,
            'TAXA DE OCUPAÇÃO MÁXIMA': [
                {'pavimentos': ['Térreo', '2º'], 'taxa': 1.0},  
                {'pavimentos': ['Demais'], 'taxa': 0.5}  
            ],
            'RECUO (m)': None,
            'TAXA DE PERMEABILIDADE MÍNIMA': None,
            'AFASTAMENTO DAS DIVISAS (m)': [
            {
            'parte': 'Embasamento comercial',
            'condicao': 'Atender o Plano Massa'
            },
            {
            'parte': 'Demais pavimentos',
            'regra': 'H/6, contado do embasamento',
            'minimo': 2.5
            }
            ],
            'LOTE PADRÃO (testada x área)': "15x450",
            'OBSERVACOES': [
                "Deverá ser implantado o Plano Massa conforme regulamentação específica.",
                "Nos terrenos situados no Eixo Estrutural Norte entre as Ruas dos Funcionários, Mal. Mascarenhas de Moraes, João Gbur e Mariano Gardolinski, e no Eixo Estrutural Sul entre as Ruas Pres. Kennedy, Orlando Padilha dos Santos até o cruzamento da Av. Winston Churchill com a Rua André Ferreira Barbosa, será limitado a 3 (três) o coeficiente de aproveitamento para o uso exclusivamente habitacional.",
                "Para as edificações de uso misto o coeficiente será igual a 4 (quatro).",
                "Taxa de Ocupação: Nos terrenos onde houver limitação de altura da edificação, em função do Cone da Aeronáutica, com subutilização do potencial, poderá, a critério do Conselho Municipal do Urbanismo - CMU, ser ampliada a taxa de ocupação, respeitados os afastamentos mínimos das divisas",
                "Taxa de permeabilidade: Atender regulamentação específica."
            ]
        },
    }
}

def get_ee_via_central_data():
    return ee_via_central

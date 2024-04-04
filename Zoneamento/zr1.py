# Criando a estrutura de dicionário para os dados da ZR1 com as informações fornecidas

# Estrutura de dicionário para ZR1
zoneamento_zr1 = {
    'Habitações Unifamiliares': {
        'COEFICIENTE DE APROVEITAMENTO': 'Básico',
        'ALTURA': 'Básico',
        'PORTE': 'Básico',
        'TAXA DE OCUPAÇÃO MÁXIMA': None,
        'TAXA DE OCUPAÇÃO MÍNIMA': 50,
        'RECUO MÍNIMO': 5,
        'TAXA DE PERMEABILIDADE MÍNIMA': 25,
        'AFASTAMENTO DAS DIVISAS MÍNIMO': None,
        'LOTE PADRÃO': '15x600'
    },
    'Habitação Unifamiliar em Série': {
        'COEFICIENTE DE APROVEITAMENTO': 1,
        'ALTURA': 2,
        # Demais parâmetros são iguais às Habitações Unifamiliares e podem ser preenchidos de forma semelhante
    },
    'Comércio e Serviço Vicinal': {
        'COEFICIENTE DE APROVEITAMENTO': None,
        'ALTURA': None,
        'PORTE': 100,
        # Demais parâmetros não especificados podem ser marcados como None ou preenchidos conforme disponíveis
    },
    'Indústria Tipo 1': {
        'COEFICIENTE DE APROVEITAMENTO': None,
        'ALTURA': None,
        'PORTE': 100,
        # Demais parâmetros não especificados podem ser marcados como None ou preenchidos conforme disponíveis
    }
}

{
 'Habitações Unifamiliares': {
  'COEFICIENTE DE APROVEITAMENTO': 'Básico',
  'ALTURA': 'Básico',
  'PORTE': 'Básico',
  'TAXA DE OCUPAÇÃO MÁXIMA': None,
  'TAXA DE OCUPAÇÃO MÍNIMA': 50,
  'RECUO MÍNIMO': 5,
  'TAXA DE PERMEABILIDADE MÍNIMA': 25,
  'AFASTAMENTO DAS DIVISAS MÍNIMO': None,
  'LOTE PADRÃO': '15x600'
 },
 'Habitação Unifamiliar em Série': {
  'COEFICIENTE DE APROVEITAMENTO': 1,
  'ALTURA': 2
  # Demais parâmetros podem ser adicionados se disponíveis
 },
 'Comércio e Serviço Vicinal': {
  'COEFICIENTE DE APROVEITAMENTO': None,
  'ALTURA': None,
  'PORTE': 100
  # Demais parâmetros podem ser adicionados se disponíveis
 },
 'Indústria Tipo 1': {
  'COEFICIENTE DE APROVEITAMENTO': None,
  'ALTURA': None,
  'PORTE': 100
  # Demais parâmetros podem ser adicionados se disponíveis
 }
}


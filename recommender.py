import pandas as pd

def calcular_pontuacao(animal, filtros, pesos):
    pontuacao = 0
    
    # Idade: pontua totalmente se estiver dentro do intervalo, caso contrário reduz pela diferença
    idade_animal = float(animal['idade']) if pd.notna(animal['idade']) else None
    if idade_animal is not None:
        if filtros['idade'][0] <= idade_animal <= filtros['idade'][1]:  # Dentro do intervalo
            pontuacao += pesos["idade"]
        else:
            # Penalidade: quanto mais longe do intervalo, menor a pontuação
            max_idade = len(filtros['idade']) - 1
            dist_min = abs(idade_animal - filtros['idade'][0])
            dist_max = abs(idade_animal - filtros['idade'][max_idade])
            penalidade = max(0, 1 - min(dist_min, dist_max) / 20)
            pontuacao += pesos["idade"] * penalidade
    
    # Porte: pontua se for exatamente igual
    pontuacao += pesos["porte"] if animal['porte'] == filtros['porte'] else 0

    # Vacinado: pontua se corresponder
    pontuacao += pesos["vacinado"] if animal['vacinado'] == filtros['vacinado'] else 0

    # Compatibilidade com outros animais
    pontuacao += pesos["bem_com_outros"] if animal['bem_com_outros'] == filtros['bem_com_outros'] else 0

    # Necessidades especiais
    pontuacao += pesos["adocao_especial"] if animal['adocao_especial'] == filtros['adocao_especial'] else 0

    # Energia: pontua mais se estiver próxima
    if pd.notna(animal['energia']):
        energia_diff = abs(animal['energia'] - filtros['energia'])
        pontuacao += pesos["energia"] * max(0, 1 - energia_diff / 2.0)
    
    return pontuacao

def recommender(df, filtros_usuario):

    # Pesos para cada critério, ajustáveis de acordo com a importância
    pesos = {
        "idade": 1.0,
        "porte": 1.5,
        "vacinado": 0.5,
        "bem_com_outros": 1.0,
        "adocao_especial": 1.0,
        "energia": 1.5
    }
    
    # Filtra os dados
    df['pontuacao'] = df.apply(lambda x: calcular_pontuacao(x, filtros_usuario, pesos), axis=1)
    
    df = df.sort_values(by='pontuacao', ascending=False)

    return df
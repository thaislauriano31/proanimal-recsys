import pandas as pd

def calcular_pontuacao(animal, filtros, pesos):
    pontuacao = 0
    
    # Idade: pontua totalmente se estiver dentro do intervalo, caso contrário reduz pela diferença
    idade_animal = float(animal['idade']) if pd.notna(animal['idade']) else None
    if idade_animal is not None:
        max_idade = len(filtros['idade']) - 1
        
        if filtros['idade'][0] <= idade_animal <= filtros['idade'][max_idade]:  # Dentro do intervalo
            pontuacao += pesos["idade"]
        
        else:
            # Penalidade: quanto mais longe do intervalo, menor a pontuação
            dist_min = abs(idade_animal - filtros['idade'][0])
            dist_max = abs(idade_animal - filtros['idade'][max_idade])
            penalidade = min(dist_min, dist_max) / 12
            pontuacao += pesos["idade"] * penalidade
    
    # Pontuam se forem exatamente iguais
    pontuacao += pesos["porte"] if animal['porte'] == filtros['porte'] else 0
    pontuacao += pesos["vacinado"] if animal['vacinado'] == filtros['vacinado'] else 0
    pontuacao += pesos["bem_com_outros"] if animal['bem_com_outros'] == filtros['bem_com_outros'] else 0
    pontuacao += pesos["adocao_especial"] if animal['adocao_especial'] == filtros['adocao_especial'] else 0

    # Energia: pontua mais se estiver próxima
    if pd.notna(animal['energia']):
        energia_diff = abs(animal['energia'] - filtros['energia'])
        pontuacao += pesos["energia"] * max(0, 1 - energia_diff)
    
    return pontuacao

def define_pesos():
    pesos = {
        "idade": 1.0,
        "porte": 1.5,
        "vacinado": 0.5,
        "bem_com_outros": 1.0,
        "adocao_especial": 1.0,
        "energia": 1.5
    }
    return pesos

def get_nota_maxima():
    pesos = define_pesos()
    return sum(pesos.values())

def recommender(df, filtros_usuario):

    # Pesos ajustáveis para cada critério
    pesos = define_pesos()

    
    df['pontuacao'] = df.apply(lambda x: calcular_pontuacao(x, filtros_usuario, pesos), axis=1)
    
    df = df.sort_values(by='pontuacao', ascending=False)

    return df

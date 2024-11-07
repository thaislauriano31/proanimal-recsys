import pandas as pd

path = 'dataset/dogs_data.csv'

# Lendo o arquivo
df = pd.read_csv(path)

# Tratando valores de idade
df['IDADE'] = df['IDADE'].str.replace(' anos', '')
df['IDADE'] = df['IDADE'].str.strip()

df['PORTE'] = df['PORTE'].str.strip()

# Se porte pequeno então substituir por 1, se medio por 2 e se grande por 3
df['PORTE'] = df['PORTE'].apply(lambda x: 1 if x.lower() == 'pequeno' else 2 if x.lower() == 'médio' else 3)

# Tratando peso
df['VACINADO'] = df['VACINADO'].apply(lambda x: 1 if x.lower() == 'sim' else 0)

df['CASTRADO'] = df['CASTRADO'].apply(lambda x: 1 if x.lower() == 'sim' else 0)

df['Se dá bem com outros animais'] = df['Se dá bem com outros animais'].apply(lambda x: 1 if x.lower() == 'não, precisa ser filho único' else 2 if x.lower() == 'só cães' else 3)

df['Adoção especial?'] = df['Adoção especial?'].apply(lambda x: 1 if x.lower() == 'sim' else 0)

df['Energia'] = df['Energia'].apply(lambda x: 1 if x.lower() == 'baixa' else 2 if x.lower() == 'média' else 3)

# Trocando nome de colunas
df.rename(columns={'NOME': 'nome'}, inplace=True)
df.rename(columns={'Raça': 'raca'}, inplace=True)
df.rename(columns={'IDADE': 'idade'}, inplace=True)
df.rename(columns={'PORTE': 'porte'}, inplace=True)
df.rename(columns={'VACINADO': 'vacinado'}, inplace=True)
df.rename(columns={'CASTRADO': 'castrado'}, inplace=True)
df.rename(columns={'Se dá bem com outros animais': 'bem_com_outros'}, inplace=True)
df.rename(columns={'Adoção especial?': 'adocao_especial'}, inplace=True)
df.rename(columns={'Energia': 'energia'}, inplace=True)
df.rename(columns={'Breve descrição': 'descricao'}, inplace=True)
df.rename(columns={'Fotos': 'tem_fotos'}, inplace=True)

# Salvando o arquivo
df.to_csv('dataset/dogs_data_tratado.csv', index=False)
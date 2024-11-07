import pandas as pd
import streamlit as st

# Carrega os dados com cache para melhor desempenho
# @st.cache_data
def load_data():
    df = pd.read_csv('dataset/dogs_data_tratado.csv')
    return df

df = load_data()

# Cabeçalho da página
col1, col2 = st.columns([1, 3])
with col1:
    st.image(".\\images\\logo.jpg", width=180)
with col2:
    st.title("Sistema de Recomendação de Adoção")
    st.subheader("Encontre o animal ideal para você!")

# Formulário para filtrar animais
with st.form("my_form"):
    st.header("Filtrar animal para adoção")

    # # Idade do animal
    idades = st.selectbox("Idade do animal", 
                         ['0 a 3', '4 a 6', '7 ou mais'],
                         help="Nota: As vezes não temos uma certeza da idade verdadeira, que é baseada em estimativas médicas"
    )

    if idades == '0 a 3':
        idades = [0,1,2,3]
    elif idades == '4 a 6':
        idades = [4,5,6]
    else:
        idade = [7, 8, 9, 10, 11, 12]
    

    # Porte do animal
    porte = st.selectbox(
        "Porte do animal",
        ["Pequeno", "Médio", "Grande"],
        help="Tamanho geral do animal, que influencia nas necessidades de espaço e cuidados"
    )

    if porte == "Pequeno":
        porte = 1
    elif porte == "Médio":
        porte = 2
    else:
        porte = 3

    # Status de vacinação
    vacinado = st.checkbox("Precisa estar vacinado",
                           help="Indica se o animal já recebeu vacinas essenciais")
    if vacinado:
        vacinado = 1
    else:
        vacinado = 0

    # Compatibilidade com outros animais
    bem_com_outros = st.selectbox("Se dá bem com outros animais",
                                  ['Com cães e gatos', 'Só cães', 'Só gatos', 'Não precisa se dar bem com cães e/ou gatos'],
                                 help="O animal convive bem com outros cães ou gatos")
    
    if bem_com_outros == 'Com cães e gatos' or bem_com_outros == 'Só gatos':
        bem_com_outros = 3
    elif bem_com_outros == 'Só cães':
        bem_com_outros = 2
    elif bem_com_outros == 'Não precisa se dar bem com cães e/ou gatos':
        bem_com_outros = 1
    

    # Necessidades especiais
    adocao_especial = st.checkbox("Necessidades de adoção especial",
                                  help="Adoção especial inclui animais com condições de saúde específicas ou necessidades únicas")
    
    if adocao_especial:
        adocao_especial = 1
    else:
        adocao_especial = 0

    # Nível de energia
    energia = st.selectbox(
        "Nível de energia",
        ["Baixa", "Média", "Alta"],
        help="Indica o nível de atividade física e mental do animal"
    )

    if energia == "Baixa":
        energia = 1
    elif energia == "Média":
        energia = 2
    else:
        energia = 3

    st.form_submit_button("Encontrar animal ideal para mim")

    # Salvar as preferências do usuário para filtragem posterior
filtros_usuario = {
    "idade": idades,
    "porte": porte,
    "vacinado": vacinado,
    "bem_com_outros": bem_com_outros,
    "adocao_especial": adocao_especial,
    "energia": energia,
}

# Exibe os filtros selecionados
st.write("Filtros selecionados:", filtros_usuario)

# Aqui, você pode adicionar a lógica para usar os filtros selecionados no modelo de recomendação
# Exemplo: filtragem do DataFrame de acordo com os filtros

filtro_df = df[
   # (df['idade'].isin(idades))
    (df['porte'] == porte)&
    (df['vacinado'] == vacinado) &
    (df['bem_com_outros'] == bem_com_outros) &
    (df['adocao_especial'] == adocao_especial) &
    (df['energia'] == energia)
]

st.write("Resultados recomendados:")
st.write(filtro_df)
import pandas as pd
import streamlit as st

# Carrega os dados com cache para melhor desempenho
# @st.cache_data
def load_data():
    df = pd.read_csv('dataset/dogs_data.csv')
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
    idade = st.selectbox("Idade do animal", 
                         ['0 a 3', '4 a 6', '6 ou mais'],
                         help="Nota: As vezes não temos uma certeza da idade verdadeira, que é baseada em estimativas médicas"
    )

    # Porte do animal
    porte = st.selectbox(
        "Porte do animal",
        ["Pequeno", "Médio", "Grande"],
        help="Tamanho geral do animal, que influencia nas necessidades de espaço e cuidados"
    )

    # Status de vacinação
    vacinado = st.checkbox("Precisa estar vacinado",
                           help="Indica se o animal já recebeu vacinas essenciais")

    # Compatibilidade com outros animais
    bem_com_outros = st.checkbox("Se dá bem com outros animais",
                                 help="O animal convive bem com outros cães ou gatos")

    # Necessidades especiais
    adocao_especial = st.checkbox("Necessidades de adoção especial",
                                  help="Adoção especial inclui animais com condições de saúde específicas ou necessidades únicas")

    # Nível de energia
    energia = st.selectbox(
        "Nível de energia",
        ["Baixa", "Média", "Alta"],
        help="Indica o nível de atividade física e mental do animal"
    )

    st.form_submit_button("Encontrar animal ideal para mim")
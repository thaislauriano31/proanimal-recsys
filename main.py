import pandas as pd
import streamlit as st
from recommender import recommender, get_nota_maxima

def load_data():
    df = pd.read_csv('dataset/dogs_data_tratado.csv')
    df['idade'] = pd.to_numeric(df['idade'], errors='coerce')
    df['energia'] = pd.to_numeric(df['energia'], errors='coerce')
    return df

def next_animal():
    st.session_state.current_index = (st.session_state.current_index + 1) % len(st.session_state.filtered_df)

def prev_animal():
    st.session_state.current_index = (st.session_state.current_index - 1) % len(st.session_state.filtered_df)

def display_animal():
    if 'filtered_df' in st.session_state:
        filtro_df = st.session_state.filtered_df
        nota_maxima = get_nota_maxima()
        current_animal = filtro_df.iloc[st.session_state.current_index]
        
        with st.container():
            st.header("Animal recomendado")
            
            st.image(f".\\images\\{current_animal['nome']}.jpg", width=175)
            st.header(current_animal["nome"])
            st.write(current_animal["descricao"])
            
            info_col1, info_col2 = st.columns(2)
            with info_col1:
                if current_animal['idade'] >= 1:
                    st.write(f"Idade: {int(current_animal['idade'])}" + (" anos" if current_animal['idade'] > 1 else " ano"))
                else:
                    st.write(f"Idade: {int(12*current_animal['idade'])}" + " meses")
                porte = {1: "Pequeno", 2: "Médio", 3: "Grande"}.get(current_animal['porte'], "Não especificado")
                st.write(f"Porte: {porte}")
            
            with info_col2:
                fit_score = round((current_animal['pontuacao'] / nota_maxima) * 100, 1)
                st.write(f"Seu fit com o animal: {fit_score}%", 
                         help="O fit indica o quão bem o animal se encaixa nos critérios que você escolheu. Pode não existir um animal com 100% de fit, então recomendamos o animal com maior fit.")
                st.write(f"Animal {st.session_state.current_index + 1} de {len(filtro_df)}")
        
            st.markdown("---")
            button_col1, button_col2, button_col3 = st.columns([1, 2, 1])
            
            with button_col2:
                col_prev, col_next = st.columns(2)
                with col_prev:
                    st.button("⬅️ Anterior", on_click=prev_animal, key='prev_button', use_container_width=True)
                with col_next:
                    st.button("Próximo ➡️", on_click=next_animal, key='next_button', use_container_width=True)

df = load_data()

# Page header
col1, col2 = st.columns([1, 3])
with col1:
    st.image(".\\images\\logo.jpg", width=175)
with col2:
    st.title("Sistema de Recomendação de Adoção da ProAnimal")
    st.subheader("Encontre o animal que mais combina com você!")

# Form for filtering animals
with st.form("my_form"):
    st.header("Filtrar animal para adoção")

    idades = st.selectbox("Idade do animal", 
                         ['0 a 3', '4 a 6', '7 ou mais'],
                         help="Nota: As vezes não temos certeza da idade verdadeira, então nos baseamos em estimativas feitas por veterinários"
    )
    idades = [0,1,2,3] if idades == '0 a 3' else [4,5,6] if idades == '4 a 6' else [7,8,9,10,11,12]

    porte_options = {"Pequeno": 1, "Médio": 2, "Grande": 3}
    porte = st.selectbox(
        "Porte do animal",
        list(porte_options.keys()),
        help="Tamanho geral do animal, que influencia nas necessidades de espaço e cuidados"
    )
    porte = porte_options[porte]

    vacinado = st.checkbox("Precisa estar vacinado",
                           help="Indica se o animal já recebeu as vacinas essenciais")
    vacinado = 1 if vacinado else 0

    castrado = st.checkbox("Precisa estar castrado",
                           help="Indica se o animal já foi castrado")
    castrado = 1 if castrado else 0

    bem_com_outros = st.selectbox("Se dá bem com outros animais?",
                                  ['Com cães e gatos', 'Só cães', 'Só gatos', 'Não precisa se dar bem com cães e/ou gatos'],
                                 help="O animal convive bem com outros cães ou gatos")
    bem_com_outros = 3 if bem_com_outros in ['Com cães e gatos', 'Só gatos'] else 2 if bem_com_outros == 'Só cães' else 1

    adocao_especial = st.checkbox("Adoção especial",
                                  help="Adoção especial inclui animais com condições de saúde específicas ou necessidades únicas")
    adocao_especial = 1 if adocao_especial else 0

    energia_options = {"Baixa": 1, "Média": 2, "Alta": 3}
    energia = st.selectbox(
        "Nível de energia",
        list(energia_options.keys()),
        help="Indica o nível de atividade física e mental do animal"
    )
    energia = energia_options[energia]

    submitted = st.form_submit_button("Encontrar animal ideal para mim")

if submitted:
    # Save user preferences
    filtros_usuario = {
        "idade": idades,
        "porte": porte,
        "vacinado": vacinado,
        "castrado": castrado,
        "bem_com_outros": bem_com_outros,
        "adocao_especial": adocao_especial,
        "energia": energia,
    }
    
    # Initialize the filtered DataFrame
    st.session_state.filtered_df = recommender(df, filtros_usuario).reset_index()
    st.session_state.current_index = 0

# Display animal information (outside the submitted condition)
display_animal()
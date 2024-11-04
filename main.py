import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    df = pd.read_csv('dataset/dogs_data.csv')
    return df

df = load_data()
   
# Page header
col1, col2 = st.columns([1, 3]) 
with col1:
    st.image(".\\images\\logo.jpg", width=180)
with col2:
    st.title("Sistema de Recomendação de Adoção")
    st.subheader("Encontre o animal ideal para você!")

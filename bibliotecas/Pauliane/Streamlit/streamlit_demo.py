import streamlit as st
import pandas as pd

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="ESQUADRÃO 5 - Streamlit",
    page_icon="🚀",
    layout="wide"
)

# TÍTULO
st.title("🚀 STREAMLIT AO VIVO")
st.subheader("Biblioteca apresentada por Pauliane")

st.write("""
Este exemplo demonstra uma aplicação web criada apenas com Python usando Streamlit.
""")

st.divider()

# INPUT
nome = st.text_input("Digite seu nome")

if st.button("Executar Demonstração"):
    st.success(f"Olá {nome}, o Streamlit está funcionando AO VIVO!")

st.divider()

# TABELA
dados = pd.DataFrame({
    "Biblioteca": ["Streamlit", "Selenium"],
    "Responsável": ["Pauliane", "Pauliane"],
    "Função": ["Dashboard Web", "Automação Web"]
})

st.subheader("Tabela Demonstrativa")
st.dataframe(dados, use_container_width=True)

st.divider()

# GRÁFICO
st.subheader("Gráfico Demonstrativo")

grafico = pd.DataFrame({
    "Projetos": [5, 10, 15, 20]
})

st.line_chart(grafico)

st.success("Demonstração concluída com sucesso.")

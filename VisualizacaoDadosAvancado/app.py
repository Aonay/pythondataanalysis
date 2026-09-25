import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configuração da página para ocupar a largura total da tela
st.set_page_config(page_title="Dashboard Global Gapminder", layout="wide")

# 2. Carregando o dataset Gapminder diretamente do Plotly
df = px.data.gapminder()

st.title("Dashboard Interativo: Desenvolvimento Socioeconômico Global")
st.markdown("Explore a relação entre riqueza, população e expectativa de vida ao redor do mundo.")

# --- BARRA LATERAL (CONTROLES DINÂMICOS) ---
st.sidebar.header("Filtros de Análise")

# Filtro 1: Seleção de Continente
continentes = sorted(df['continent'].unique().tolist())
continente_selecionado = st.sidebar.selectbox("Selecione o Continente", continentes)

# Filtrando o DataFrame com base no continente escolhido
df_filtrado_continente = df[df['continent'] == continente_selecionado]

# Filtro 2: Seleção de Ano (Slider dinâmico)
anos_disponiveis = sorted(df_filtrado_continente['year'].unique())
ano_selecionado = st.sidebar.slider(
    "Selecione o Ano", 
    min_value=min(anos_disponiveis), 
    max_value=max(anos_disponiveis), 
    step=5,
    value=max(anos_disponiveis) # Valor inicial padrão no último ano
)

# Filtrando os dados finais para o continente e ano específicos
df_final = df_filtrado_continente[df_filtrado_continente['year'] == ano_selecionado]


# --- CORPO DO DASHBOARD (LAYOUT EM DUAS COLUNAS) ---
coluna1, coluna2 = st.columns(2)

with coluna1:
    st.subheader(f"PIB per Capita vs Expectativa de Vida ({ano_selecionado})")
    
    # Gráfico de dispersão dinâmico
    fig_scatter = px.scatter(
        df_final,
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="country",
        hover_name="country",
        log_x=True,
        size_max=60,
        height=500
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

with coluna2:
    st.subheader(f"Top 10 Maiores Populações em {ano_selecionado}")
    
    # Selecionando os 10 maiores países em população do recorte atual
    top_populacao = df_final.nlargest(10, 'pop')
    
    # Gráfico de barras dinâmico
    fig_bar = px.bar(
        top_populacao,
        x="country",
        y="pop",
        color="country",
        text_auto='.2s',
        height=500
    )
    st.plotly_chart(fig_bar, use_container_width=True)
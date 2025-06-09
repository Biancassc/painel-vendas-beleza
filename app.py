import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

st.set_page_config(layout="wide", page_title="Painel de Vendas de Produtos de Beleza")
st.title("Painel de Vendas - Cosméticos e Produtos de Beleza")

@st.cache_data
def carregar_dados():
    dim_produto = pd.read_csv("dim_produto.csv")
    dim_cliente = pd.read_csv("dim_cliente.csv")
    dim_vendedor = pd.read_csv("dim_vendedor.csv")
    dim_fornecedor = pd.read_csv("dim_fornecedor.csv")
    fato_vendas = pd.read_csv("fato_vendas.csv", parse_dates=['data_venda'])

    df = fato_vendas \
        .merge(dim_produto, on="id_produto") \
        .merge(dim_cliente, on="id_cliente") \
        .merge(dim_vendedor, on="id_vendedor") \
        .merge(dim_fornecedor, on="id_fornecedor")

    return df

df = carregar_dados()

st.sidebar.header("Filtros")
periodo = st.sidebar.date_input("Período", [df['data_venda'].min(), df['data_venda'].max()])
estados = st.sidebar.multiselect("Estados", df['estado'].unique(), default=df['estado'].unique())

df_filtro = df[
    (df['data_venda'] >= pd.to_datetime(periodo[0])) &
    (df['data_venda'] <= pd.to_datetime(periodo[1])) &
    (df['estado'].isin(estados))
]

if st.sidebar.checkbox("Exibir dados brutos"):
    st.subheader("Dados completos (antes do filtro)")
    st.write(df.head())

    st.subheader("Dados filtrados")
    st.write(df_filtro.head())

aba = st.sidebar.radio("Selecione a Aba", ["Vendas", "Produtos e Clientes", "Relatórios"])

if aba == "Vendas":
    st.subheader("Gráfico de Vendas por Data")
    vendas_dia = df_filtro.groupby('data_venda')['valor_total'].sum().reset_index()
    fig1 = px.line(vendas_dia, x='data_venda', y='valor_total', title="Evolução Diária das Vendas")
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("Gráfico de Vendas por Vendedor")
    vendas_vendedor = df_filtro.groupby('nome_vendedor')['valor_total'].sum().reset_index()
    fig2 = px.bar(vendas_vendedor, x='nome_vendedor', y='valor_total', title="Total por Vendedora")
    st.plotly_chart(fig2, use_container_width=True)

elif aba == "Produtos e Clientes":
    st.subheader("Distribuição de Vendas por Produto")
    fig3 = px.pie(df_filtro, names='nome_produto', values='valor_total', title="Distribuição de Vendas por Produto")
    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("Top Clientes por Faturamento")
    top_clientes = df_filtro.groupby('nome_cliente')['valor_total'].sum().reset_index().sort_values(by='valor_total', ascending=False)
    fig4 = px.bar(top_clientes, x='nome_cliente', y='valor_total', title="Top Clientes por Faturamento")
    st.plotly_chart(fig4, use_container_width=True)

elif aba == "Relatórios":
    st.subheader("Total de Vendas por Estado")
    vendas_estado = df_filtro.groupby("estado")['valor_total'].sum().reset_index()
    fig5 = px.bar(vendas_estado, x="estado", y="valor_total", title="Total de Vendas por Estado")
    st.plotly_chart(fig5, use_container_width=True)

    st.subheader("Total de Vendas por Cidade")
    vendas_cidade = df_filtro.groupby("cidade")['valor_total'].sum().reset_index()
    fig6 = px.bar(vendas_cidade, x="cidade", y="valor_total", title="Total de Vendas por Cidade")
    st.plotly_chart(fig6, use_container_width=True)

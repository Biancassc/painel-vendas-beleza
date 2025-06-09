import pandas as pd
import os

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

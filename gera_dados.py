import pandas as pd
from datetime import datetime, timedelta
import random

def gerar_dados_dimensoes():
    produtos = pd.DataFrame({
        'id_produto': range(1, 6),
        'nome_produto': [
            'Base Líquida Fran',
            'Rímel-Boca Rosa',
            'Vitamina C- Principia',
            'Hidratante Dove',
            'Pó Translúcido-Boca Rosa'
        ],
        'id_fornecedor': [1, 2, 3, 1, 2]
    })

    clientes = pd.DataFrame({
        'id_cliente': range(1, 5),
        'nome_cliente': ['Carla Lima', 'Juliana Silva', 'Fernanda Dias', 'Amanda Costa'],
        'estado': ['RJ', 'PB', 'PE', 'RN'],
        'cidade': ['Niterói', 'João Pessoa', 'Recife', 'Natal']
    })

    vendedores = pd.DataFrame({
        'id_vendedor': range(1, 4),
        'nome_vendedor': ['Bruna', 'Camila', 'Paula']
    })

    fornecedores = pd.DataFrame({
        'id_fornecedor': range(1, 4),
        'nome_fornecedor': ['Fran Cosméticos', 'Boca Rosa Beauty', 'Principia Skincare']
    })

    vendas = []
    for i in range(200):
        data = datetime(2023, 1, 1) + timedelta(days=random.randint(0, 364))
        id_produto = random.randint(1, 5)
        id_cliente = random.randint(1, 4)
        id_vendedor = random.randint(1, 3)
        quantidade = random.randint(1, 5)
        preco = round(random.uniform(50, 500), 2)
        total = round(quantidade * preco, 2)
        vendas.append([i+1, data, id_produto, id_cliente, id_vendedor, quantidade, preco, total])

    df_vendas = pd.DataFrame(vendas, columns=[
        'id_venda', 'data_venda', 'id_produto', 'id_cliente', 'id_vendedor', 'quantidade', 'preco_unitario', 'valor_total'
    ])

    produtos.to_csv('dim_produto.csv', index=False)
    clientes.to_csv('dim_cliente.csv', index=False)
    vendedores.to_csv('dim_vendedor.csv', index=False)
    fornecedores.to_csv('dim_fornecedor.csv', index=False)
    df_vendas.to_csv('fato_vendas.csv', index=False)

gerar_dados_dimensoes()

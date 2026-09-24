import pandas as pd

#importando Dataset

df= pd.read_csv("Vendas.csv")
print(df.head())
print(df.info())
print(df.describe())

#Processamento automatico de dados

vendasProduto = df.groupby(["Produto","Estado"])["Quantidade"].sum().reset_index()
print(vendasProduto)

#gerando um relatorio

vendasProduto.to_csv("ProdutosEstado.csv", index=False, encoding="utf-8-sig")
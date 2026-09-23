import pandas as pd

dados = {
  "Produto":["Notebook","Mouse","Teclado"],
  "Preço":[2500,380,180]
}

df = pd.DataFrame(dados)
print(df)

print(df["Produto"])

media  = df["Preço"].mean() # calcula a média
print(media)

quantidade = df["Produto"].count() # calcula a quantidade de valores validos
print(quantidade)

descricao = df.describe() # tras uma relação de estatisticas do dataframe
print(descricao)

informacoes = df.info()

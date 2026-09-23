import numpy as np
import pandas as pd

numeros = np.array([1,2,3,5,6])
resultado = numeros * 2
print(resultado)

dados = {
  "Produto":["Notebook","Mouse","Teclado"],
  "Preço":[2500,380,180]
}

df = pd.DataFrame(dados)
print(df)

df.to_csv("dados.csv", index=False)
df2= pd.read_csv("dados.csv")
print(df2)
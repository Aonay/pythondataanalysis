# O Numpy ele trabalha com arrays e operacoes numericas
# O Padas serve pra trabalhar com dados, plnilhas tabelas, banco de dados etc
# Matplolib torna resultados visiveis atraves de graficos

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


array = np.array([1,2,3,4,5])
print(array)

dados = {
  "nome":["Ana","Carlos","Maria"],
  "idade":[25,38,18]
}

df = pd.DataFrame(dados)
print(df)

x = [1,2,3,4,5]
y = [10,20,25,30,32]

plt.plot(x,y)
plt.show()
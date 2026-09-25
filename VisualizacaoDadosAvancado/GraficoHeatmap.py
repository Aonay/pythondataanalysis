import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/tips.csv"

df = pd.read_csv(url)

#Heatmap ou mapa de calor é usado quando eu quero comparar varias variaveis numericas ao mesmo tempo.
#Nesse grafico o 1 é o valor mais alto de correlacao logo na diagonal quando a varivel se compara com ela mesma sempre vai ser 1

correlacao = df.corr(numeric_only=True)

plt.figure(figsize=(8,6))

sns.heatmap(
  correlacao,
  annot=True,
  cmap="coolwarm"
)

plt.title("Correlacao entre variaveis")

plt.show()
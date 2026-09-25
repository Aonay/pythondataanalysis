import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/tips.csv"

df = pd.read_csv(url)

#Grafico de Dispersao - E usado para identificar se existe alguma relacao entre as variaveis.

#Exemplo com matplotlib

plt.scatter(df["total_bill"],df["tip"])
plt.xlabel("Conta Total")
plt.ylabel("Valor da Gorjeta")
plt.title("Relacao Conta e Gorjeta")
plt.show()

#Exemplo com seaborn


sns.scatterplot(data=df,x="total_bill", y="tip")
plt.show()


#Exemplo com plotly

fig = px.scatter(
  df,
  x="total_bill",
  y="tip",
  color="day",
  title="Relacao entre conta e gorjeta"
)

fig.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/tips.csv"

df = pd.read_csv(url)

#Grafico de Barras

plt.figure(figsize=(8,5)) #estou definindo a proporcao do grafico

plt.bar(df["day"],df["tip"], color="green")

plt.title("Gorjetas por dia")

plt.xlabel("Dia")
plt.ylabel("Gorjeta")

plt.show()


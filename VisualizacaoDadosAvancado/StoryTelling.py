import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/tips.csv"

df = pd.read_csv(url)

# Definindo um tema visual limpo e profissional
sns.set_theme(style="whitegrid")

# Criando uma grade de 2 linhas por 2 colunas para contar a historia sequencialmente
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))

# --- CAPITULO 1: A relacao direta entre o consumo e a gorjeta ---
sns.scatterplot(
    data=df, 
    x="total_bill", 
    y="tip", 
    hue="time", 
    alpha=0.8, 
    palette="deep",
    ax=axes[0, 0]
)
axes[0, 0].set_title("Capitulo 1: Contas Maiores geram Gorjetas Maiores?")
axes[0, 0].set_xlabel("Valor Total da Conta")
axes[0, 0].set_ylabel("Valor da Gorjeta")

# --- CAPITULO 2: O comportamento financeiro por dia da semana ---
ordem_dias = ['Thur', 'Fri', 'Sat', 'Sun']
sns.barplot(
    data=df, 
    x="day", 
    y="tip", 
    order=ordem_dias, 
    palette="Blues_d", 
    ax=axes[0, 1]
)
axes[0, 1].set_title("Capitulo 2: Media de Gorjetas por Dia da Semana")
axes[0, 1].set_xlabel("Dia da Semana")
axes[0, 1].set_ylabel("Gorjeta Media")

# --- CAPITULO 3: Comparando turnos (Almoco vs Jantar) ---
sns.boxplot(
    data=df, 
    x="time", 
    y="total_bill", 
    palette="Set2", 
    ax=axes[1, 0]
)
axes[1, 0].set_title("Capitulo 3: Amplitude de Gastos por Turno")
axes[1, 0].set_xlabel("Turno")
axes[1, 0].set_ylabel("Valor Total da Conta")

# --- CAPITULO 4: O impacto do tamanho da mesa no consumo ---
sns.barplot(
    data=df, 
    x="size", 
    y="tip", 
    palette="Purples_d", 
    ax=axes[1, 1]
)
axes[1, 1].set_title("Capitulo 4: Conta Media por Tamanho da Mesa")
axes[1, 1].set_xlabel("Numero de Pessoas na Mesa")
axes[1, 1].set_ylabel("Gorjeta Media")

# Ajustando o espacamento entre os graficos para evitar sobreposicao
plt.tight_layout()
plt.show()
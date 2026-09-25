import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/tips.csv"

df = pd.read_csv(url)

fig, ax = plt.subplots(1,2, figsize=(10,4))

sns.histplot(df["total_bill"],ax=ax[0],kde=True,color="blue")
ax[0].set_title("Distribuicao da Conta")

sns.boxplot(data=df, x="day", y="tip", ax=ax[1],palette="Set2")
ax[1].set_title("Gorjetas por dia")

plt.show()
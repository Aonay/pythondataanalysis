import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/tips.csv"

df = pd.read_csv(url)

print(df.head())





import pandas as pd
import numpy as np

#1 Carregando
#2 Limpar dados
#3 Transformar Dados
#$ Gerar Dataset final


df = pd.read_csv("dataset/Titanic-Dataset.csv")
print(df.head())

# metodo para gerar um pipeline 

def limpar_dados(df):
  df["Age"].fillna(df["Age"].mean(), inplace=True)

  df["Fare_normalized"] = (
    df["Fare"] - df["Fare"].min()
  ) / (df["Fare"].max() - df["Fare"].min())

  return df

#metodo para validar um dataset vizualizando informações importantes

def validar_dataset(df):
  print("Linhas:", df.shape[0])
  print("Colunas:", df.shape[1])
  print("\nValores ausentes:")
  print(df.isnull().sum())


limpar_dados(df)
print(df["Age"],df["Fare_normalized"])

validar_dataset(df)








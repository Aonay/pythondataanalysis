import pandas as pd
#Importando Dataset do Titanic 
# pd.set_option('display.max_columns', None) # immpede uqe no concole oculte colunas  (...)

df = pd.read_csv("dataset/Titanic-Dataset.csv")

print("Exibicao apenas das 5 primeiras linhas e alguams colunas")
print(df.head()) # Usado pra ter uma visao pra ver algumas linhas e colunas retornas os 5 primeiros registros.

print("Tamanho do Dataset")
print(df.shape) #Exibe o tamanho do dataset

print("Visualizando resumo geral co df.info()")
print(df.info())

print("Vizualiando com df.describe")
print(df.describe())

#Tratamento de Valores Ausenes NaN
print(df.isnull().sum()) #exibe a soma dos valores ausentes de cada coluna

#Removendo valores ausentes

df_dropna= df.dropna() #remove registros que nao tem todos os valroes preenchidos nas colunas

print(df_dropna.info())

#Preenchendo valores ausentes

df["Age"] = df["Age"].fillna(df["Age"].mean()) # o motodo fillna() inclui valores em celulas vazias e no caso estamos alterando a coluna Age pegando ela mesmo e calculando a media

print(df.isnull().sum())
print(df.head())


#NORMALIZCAO E PADRONIZACAO
#Criando nova coluna com valores baseados em outra

df["Age-Log"] = df["Age"].apply(lambda x:x) # o apply é usando pra aplicar funcoes em celulas, lambda é uma funcao de uma linha , em outras palavras estamos criando uma cópia identica da coluna ja que x é igual a x

print(df["Age-Log"])

# quando valores de variaveis estao com as escala muito distoantes usamos a normalização, umas das tecnicnas é o min/max faremos isso com "fare" (colua tarifa)

df["Fare_normalized"] = (df["Fare"] - df["Fare"].min()) / (df["Fare"].max() - df["Fare"].min())
print(df["Fare_normalized"])
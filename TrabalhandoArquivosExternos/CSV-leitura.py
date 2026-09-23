import csv

with open("arquivos/pessoas.csv", "r")as arquivo:
  leitura = csv.reader(arquivo)
  for linha in leitura:
    print(linha)
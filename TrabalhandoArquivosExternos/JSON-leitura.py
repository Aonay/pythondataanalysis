import json

with open("arquivos/pessoas2.json","r") as arquivo:
  dados = json.load(arquivo)
  print(dados)
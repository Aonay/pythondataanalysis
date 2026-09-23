#criando e usando um arquivo csv no codigo

import csv

dados = [
  ["nome","idade","jogo"],
  ["Julio",30, "Conter Strike"],
  ["Vanessa",28,"Fortnite"],
  ["Pedro",25,"League of Legens"]
]

# o parametro newline impede que linhas em branco sejam incluidas

with open("arquivos/pessoas.csv","w", newline="") as arquivo:
  writer = csv.writer(arquivo) #criando o csv na variavel
  writer.writerows(dados)  #Crindo os registros no arquivo
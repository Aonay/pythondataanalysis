#o codigo nessa classe sempre vai executar independente de acontecer um erro ou nao
#exemplo

try:
  numero= int("10")
  print(numero)
except ValueError:
  print("Erro de conversao")
finally:
  print("Execucao finalizada")
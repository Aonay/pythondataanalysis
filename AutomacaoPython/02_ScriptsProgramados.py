import datetime

def executar_relatorio():
  agora = datetime.datetime.now()
  print("Gerando relatorio...")
  print("Horario:", agora)

executar_relatorio()

def gerar_relatorio():
  vendas = [120,20,300,750]
  total = sum(vendas)
  agora = datetime.datetime.now()

  print("Relatorio gerado em:", agora)
  print("Total em vendas:",total)

gerar_relatorio()
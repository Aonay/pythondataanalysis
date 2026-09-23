import sqlite3

with sqlite3.connect("dados.db") as conexao:
  cursor = conexao.cursor()

  cursor.execute(
    "SELECT * FROM usuarios"
  )

  dados = cursor.fetchall()

  print(dados)
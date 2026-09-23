import sqlite3

conexao = sqlite3.connect("dados.db")

cursor = conexao.cursor()

""" cursor.execute(
  "INSERT INTO usuarios VALUES (?,?)",
  ("Ana",25)
) """

# Inserindo vários de uma vez (excelente para grandes volumes de dados)
novos_usuarios = [("João", 30), ("Maria", 22), ("Carlos", 40)]
cursor.executemany("INSERT INTO usuarios VALUES (?, ?)", novos_usuarios)

conexao.commit()
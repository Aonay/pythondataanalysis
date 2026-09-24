import sqlite3

conn = sqlite3.connect("dados.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
nome TEXT,
idade INTEGER
)
""")

conn.commit()

print("Tabela criada com sucesso")

cursor.execute(
  "INSERT INTO usuarios VALUES (?,?)",
  ("ANA",25)
)

conn.commit()
print("Usuario inserido com sucesso")

cursor.execute(
  "SELECT * FROM usuarios"
)

dados=cursor.fetchall()
print("Usuaros no banco:")
for usuario in dados:
  print(usuario)


conn.close()
print("Conexao concluida com sucesso")
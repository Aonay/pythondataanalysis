import sqlite3

# sqlite3 vem nativo no python

conexao = sqlite3.connect("dados.db") #cria uma ligacao do programa com o arquivo do banco de dados, se nao existir cria um

cursor = conexao.cursor() #cursor vai ser o objeto para enviar o comandos pro bando de dados.

cursor.execute("""
CREATE TABLE usuarios (
nome TEXT,
idade INTEGER
)
""")

conexao.commit()


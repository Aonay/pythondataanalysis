# a funcao OPEN é usada pra trabalhar com arquivos, usado juntamente com with que automaticamente salva e fecha o arquivo automaticamente ao encerrar o bloco de codigo

with open("arquivos/leitura.txt", "r", encoding="utf-8") as arquivo:
  conteudo = arquivo.read()
  #a funcao read() - le todo o arquivo
print(conteudo)
print("------------------------fim-----------------------")

# lendo linha por linha

with open("arquivos/leitura.txt", "r", encoding="utf-8")as arquivo:
  for linha in arquivo:
    print(linha.strip())

#função write() para escrever no arquivo - escreve no arquivo. o parametro "w" em open() criar um arquivo ou sobreescreve, ja o "a" adiciona ao final

with open("arquivos/gravação.txt","a") as arquivo:
  arquivo.write("Estudando python para trabalhar com dados\n")
  arquivo.write("Estudando python para ganhar dinheiro com dados\n")
  arquivo.write("Estudando python para me sustentar com dados\n")
  arquivo.write("Estudando python para ser engenheiro de dados\n")


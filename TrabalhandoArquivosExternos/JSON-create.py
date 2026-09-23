import json

dados = [
    {
        "Nome": "Ana Silva",
        "Idade": 28,
        "Cidade": "São Paulo",
        "Profissão": "Engenheira"
    },
    {
        "Nome": "Bruno Costa",
        "Idade": 34,
        "Cidade": "Rio de Janeiro",
        "Profissão": "Professor"
    },
    {
        "Nome": "Carla Souza",
        "Idade": 22,
        "Cidade": "Belo Horizonte",
        "Profissão": "Designer"
    },
    {
        "Nome": "Diego Alves",
        "Idade": 40,
        "Cidade": "Curitiba",
        "Profissão": "Desenvolvedor"
    },
    {
        "Nome": "Elena Gomes",
        "Idade": 29,
        "Cidade": "Porto Alegre",
        "Profissão": "Médica"
    }
]

with open("arquivos/pessoas2.json", "w") as arquivo:
  json.dump(dados,arquivo)
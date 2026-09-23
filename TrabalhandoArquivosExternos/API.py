#Protocolos http

#Biblioteca para requisicoes REQUESTS

import requests,json

url = "https://rickandmortyapi.com/api/character/?name=morty"

resposta = requests.get(url)
# 1. É sempre bom garantir que a requisição deu certo (Status 200 = OK)
if resposta.status_code == 200:
    
    # 2. Convertendo a resposta bruta para um Dicionário Python
    dados = resposta.json()
    
    # 3. Entrando na chave 'results', que guarda a lista de personagens
    lista_personagens = dados['results']
    
    # 4. Pegando o primeiro personagem da lista (índice 0)
    primeiro_morty = lista_personagens[0]
    
    # 5. Extraindo apenas os dados que nos interessam
    nome = primeiro_morty['name']
    status = primeiro_morty['status']
    especie = primeiro_morty['species']
    origem = primeiro_morty['origin']['name'] # Dicionário dentro de dicionário!
    
    print("--- Ficha do Personagem ---")
    print(f"Nome: {nome}")
    print(f"Status: {status}")
    print(f"Espécie: {especie}")
    print(f"Planeta de Origem: {origem}")

    with open("arquivos/FichaMorty.json", "w") as arquivo:
        json.dump(dados, arquivo)

else:
    print(f"A API falhou. Código de erro: {resposta.status_code}")


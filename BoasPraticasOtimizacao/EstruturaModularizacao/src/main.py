#CHAMAR FUNCOES E DEFINIR ORDEM DAS ETAPAS
from utils import calcular_imc, formatar_moeda

# Usando as funções importadas
meu_imc = calcular_imc(102, 1.92)
print(f"Meu IMC é: {meu_imc:.2f}")

preco_formatado = formatar_moeda(1500.50)
print(preco_formatado)
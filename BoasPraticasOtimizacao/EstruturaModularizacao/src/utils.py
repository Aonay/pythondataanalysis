#CALCULOS E FUNCOES
# utils.py

def calcular_imc(peso, altura):
    """Calcula o Índice de Massa Corporal."""
    return peso / (altura ** 2)

def formatar_moeda(valor):
    """Formata um número para o padrão monetário brasileiro."""
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
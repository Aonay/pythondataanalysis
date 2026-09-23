import pandas as pd

dados_funcionarios = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo'],
    'Departamento': ['TI', 'Vendas', 'TI', 'RH', 'Vendas'],
    'Idade': [28, 34, 29, 42, 38],
    'Salario': [7500.00, 6200.00, 8100.00, 5400.00, 7100.00],
    'Ativo': [True, True, False, True, True]
}

df = pd.DataFrame(dados_funcionarios)
print(df)

#Usando .mean quando ha colunas de text. é preciso infomar somente as numericas que ser saber a media
agrupados1 = df.groupby("Departamento")[['Idade', 'Salario']].mean()
print("--- Média de Idade e Salário por Departamento DECLARANDO ---")
print(agrupados1)

agrupados2 = df.groupby("Departamento").mean(numeric_only=True)
print("--- Média de Idade e Salário por Departamento ACEITANDO TODAS NUMERICAS ---")
print(agrupados2)

# Quando temos dataframes com dados mistos é comum se usar  .agg() (Aggregation). Ele permite que você faça perguntas diferentes para colunas diferentes em uma única linha de código, criando relatórios analíticos completos.

relatorio_departamentos = df.groupby("Departamento").agg({
    'Nome': 'count',       # Conta quantos funcionários têm no departamento
    'Idade': 'mean',       # Pega a média de idade
    'Salario': ['min', 'max', 'mean'], # Pega o menor, o maior e a média salarial!
    'Ativo': 'sum'         # Soma os ativos (True vale 1, False vale 0)
})

print("\n--- Relatório Analítico Profissional ---")
print(relatorio_departamentos)
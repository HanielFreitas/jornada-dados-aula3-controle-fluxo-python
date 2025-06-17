### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]

total_por_categoria = {}
for venda in vendas:

    if venda["categoria"] in total_por_categoria:
        total_por_categoria[venda["categoria"]] += venda["valor"]
    else:
        total_por_categoria[venda["categoria"]] = venda["valor"]

print(total_por_categoria)
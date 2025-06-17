### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

numeros = range(1, 11)

for i in numeros:
    if i % 2 == 0:
        print(f'{i} é um número Par') 

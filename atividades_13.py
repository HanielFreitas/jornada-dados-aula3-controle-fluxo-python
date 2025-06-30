### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

pagina_inicial = 1
pagina_final = 5

while pagina_inicial <= pagina_final:
    print(f"Processando página {pagina_inicial} de {pagina_final}")
    pagina_inicial += 1

print("Todas as páginas foram processadas.")
### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

texto = 'Alice no Pais das Maravilhas no mundo mágico de Alice'
texto_esp = texto.lower().split()

cont = {}

for p in texto_esp:
    if p in cont:
        cont[p] += 1
    else:
        cont[p] = 1
print(cont)



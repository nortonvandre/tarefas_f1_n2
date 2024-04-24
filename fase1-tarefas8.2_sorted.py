lista = [1, 4, 2, 7, 3]

# Loop para percorrer cada elemento da lista
for i in range(len(lista)):
    # Loop interno para comparar o elemento atual com os elementos seguintes
    for j in range(i+1, len(lista)):
        # Se o elemento atual for menor que o próximo elemento, trocamos os elementos
        if lista[i] < lista[j]:
            lista[i], lista[j] = lista[j], lista[i]

# Imprime a lista ordenada em ordem decrescente
print(lista)

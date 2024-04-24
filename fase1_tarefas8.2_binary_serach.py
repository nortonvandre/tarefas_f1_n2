def search(lista, valor):
    """
    Busca um valor em uma lista ordenada utilizando o algoritmo de busca binária.
    
    Parâmetros:
    - lista: lista de números inteiros ordenados
    - valor: número inteiro a ser buscado na lista
    
    Retorna:
    - Índice do valor na lista, se encontrado; caso contrário, retorna -1
    """
    
    inicio = 0
    fim = len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        
        # Verifica se o valor do meio é igual ao valor de busca
        if lista[meio] == valor:
            return meio  # Retorna o índice do valor encontrado
        
        # Se o valor do meio for menor que o valor de busca, atualiza o inicio
        elif lista[meio] < valor:
            inicio = meio + 1
            
        # Se o valor do meio for maior que o valor de busca, atualiza o fim
        else:
            fim = meio - 1
            
    return None  # Retorna -1 se o valor não for encontrado

# Lista de números ordenados
lista = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
valor = 14

# Chama a função de busca binária e imprime o resultado
indice = search(lista, valor)

if indice is not None:
    print(f"O valor {valor} foi encontrado no índice {indice}.")
else:
    print(f"O valor {valor} não foi encontrado")

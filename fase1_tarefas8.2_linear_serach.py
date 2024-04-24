def search(arr, length, x):
    """
    Busca um elemento em um array e retorna o elemento se encontrado ou None caso contrário.
    
    Parâmetros:
    arr (list): Lista de elementos onde a busca será realizada.
    length (int): Tamanho da lista de elementos.
    x: Elemento a ser buscado na lista.
    
    Retorna:
    O elemento buscado se encontrado, ou None caso contrário.
    """
    
    # Percorre o array até o tamanho especificado
    for i in range(length):
        # Verifica se o elemento atual é igual ao elemento buscado
        if arr[i] == x:
            return arr[i]  # Retorna o elemento encontrado
    
    return None  # Retorna None se o elemento não for encontrado

# Lista de números
arr = [10, 20, 30, 40, 50]

# Elemento a ser buscado
x = 20

# Tamanho da lista
length = len(arr)

# Chama a função de busca e imprime o resultado
print(search(arr, length, x))

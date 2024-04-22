def rotaçao(arr,count):
    lista = arr
    numero_removido = 0
    k = count
    for c in range(len(lista)-k,0,-1):
        if k ==0:
            break
    
        numero_removido = lista.pop()
        lista.insert(0,numero_removido)
        k-=1
    return lista
    

arr = [2,3,4,5,6,7,8,9,10]
count = 2
print(f"lista original: {arr}")
print(f"lista em rotaçao {count}: {rotaçao(arr,count)}")

    



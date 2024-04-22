# Lista de números
numeros = [10, 4, 3, 50, 23, 90]

maior1 = 0
maior2 = 0
maior3 = 0

# Percorre a lista para encontrar os três maiores números
for num in numeros:
    if num > maior1:
        maior3 = maior2
        maior2 = maior1
        maior1 = num
    elif num > maior2 and num != maior1:
        maior3 = maior2
        maior2 = num
    elif num > maior3 and num != maior2 and num != maior1:
        maior3 = num

print(f"Os três maiores números são: {maior1}, {maior2}, {maior3}")

palavras = "GeeKs01fOr@gEEks07"


upper , lower , num, especial = 0,0,0,0

for palavra in palavras:

    if palavra.isupper():
        upper +=1
    elif palavra.islower():
        lower +=1
    elif palavra.isdigit():
        num +=1
    else:
        especial +=1

print(upper)
print(lower)
print(num)
print(especial)
def caracter(p):
    palavra = p
    letras ="abcdefghijklmnopqrstuwyxz"
    letra_s = ''
    for letra in letras:
        if not letra in palavra:
            letra_s += letra
    return letra_s


palavra = "balao"
print(caracter(palavra))

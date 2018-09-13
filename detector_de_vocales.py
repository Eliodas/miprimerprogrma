
vocales=["a","e","i","o","u"]
vocales_frase=[]


frase_usuario=input("Introduzca frase: ")

for item in frase_usuario:
    if item in vocales:
        vocales_frase.append(item)

print("Vocales = {}" .format(vocales_frase))
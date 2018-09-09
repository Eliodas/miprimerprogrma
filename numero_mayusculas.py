
frase_usuario=input("Escriba una frase")

contador_mayusculas=0

for letra in frase_usuario:
    if letra==letra.upper() and letra.upper() != letra.lower():
        contador_mayusculas += 1

print("mayusculas = {}" . format(contador_mayusculas))
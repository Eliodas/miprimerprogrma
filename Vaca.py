

frase_usuario="Mama huevo,la gallina"
posiciones=""
letras=["a","e","i","o","u"]
i=1
for l in frase_usuario:
    if l in letras:
        posiciones+=str(i)
        i+=1
    else: posiciones+=l

print(posiciones)
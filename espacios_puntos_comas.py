

frase_del_usuario=input("Introduce la frase que quieras: ")

espacios=0
comas=0
puntos=0

for caracter in frase_del_usuario:
    if caracter==' ':
        espacios+=1
    elif caracter == ',':
        comas+=1
    elif caracter == '.':
        puntos+=1

print("espacios = {} \ncomas = {} \npuntos = {} ".format(espacios,comas,puntos))
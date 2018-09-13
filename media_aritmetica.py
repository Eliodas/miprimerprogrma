
numeros_usuario=[]

numero_del_usuario=""

while len(numeros_usuario) < 10:
    while not numero_del_usuario.isdigit():
        numero_del_usuario=input("Introduzca numero: ")
    numeros_usuario.append(int(numero_del_usuario))
    numero_del_usuario=""
    print("¡Numero añadido!")

suma=0
i=0
for sumando in numeros_usuario:
    suma+=sumando
    i+=1

print("La media es: {}".format((suma/i)))
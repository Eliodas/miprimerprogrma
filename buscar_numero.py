

numeros_usuario=[]

numero_del_usuario=""

while len(numeros_usuario) < 10:
    while not numero_del_usuario.isdigit():
        numero_del_usuario=input("Introduzca numero: ")
    numeros_usuario.append(int(numero_del_usuario))
    numero_del_usuario=""
    print("¡Numero añadido!")

numero_peque=numeros_usuario[0]

for numero in numeros_usuario:
    if numero_peque>numero:
        numero_peque=numero

print("El numero mas pequeño es {}" .format(numero_peque))

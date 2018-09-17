
numeros_usuario=[]

numero_del_usuario=""

for n in range(1,11):
    while not numero_del_usuario.isdigit():
        numero_del_usuario=input("Introduzca numero: ")
    numeros_usuario.append(int(numero_del_usuario))
    numero_del_usuario=""
    print("¡Numero añadido!")

multiplicado=1
for multiplicador in numeros_usuario:
    multiplicado*=multiplicador

print(multiplicado)
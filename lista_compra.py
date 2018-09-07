from builtins import print

mi_lista=[]
input_usuario=""
numero_lista=0

input_usuario=input("Que quieres comprar?: (Escriba FIN para acabar)")
mi_lista.append(input_usuario)

while input_usuario.upper() != "FIN":

    input_usuario=input("Que quieres comprar?: (Escriba FIN para acabar)")
    mi_lista.append(input_usuario)

if len(mi_lista)!=1:
    print("Tengo que comprar:")

while numero_lista < len(mi_lista)-1:
    print(mi_lista[numero_lista])
    numero_lista+=1
from builtins import print

mi_lista=[]
numero_lista=0

input_usuario=input("Que quieres comprar?: (Escriba FIN para acabar)")


while input_usuario.upper() != "FIN":
    mi_lista.append(input_usuario)
    input_usuario=input("Que quieres comprar?: (Escriba FIN para acabar)")


if len(mi_lista)!=0:
    print("Tengo que comprar:")

while numero_lista < len(mi_lista):
    print(mi_lista[numero_lista])
    numero_lista+=1
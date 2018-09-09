from builtins import print

mi_lista=[]

input_usuario=input("Que quieres comprar?: (Escriba FIN para acabar)")

while input_usuario.upper() != "FIN":
    mi_lista.append(input_usuario)
    input_usuario=input("Que quieres comprar?: (Escriba FIN para acabar)")

for item in mi_lista:
    print("tengo que comprar {}".format(item))
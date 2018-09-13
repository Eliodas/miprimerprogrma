
lista=[]

elemento_lista=input("Escribe un elemento: (Escriba fin si quiere acabar la lista)")

while elemento_lista.upper() != "FIN":
    lista.append(elemento_lista)
    elemento_lista = input("Escribe un elemento: (Escriba fin si quiere acabar la lista")

i=0
for numero in lista:
    i+=1

print("largo_lista={}".format(i))


lista=["hola",23,"me llamo",14,"willyrex",87]
lista_str=[]
lista_int=[]

for item in lista:
    if type(item) is str:
        lista_str.append(item)
    elif type(item) is int:
        lista_int.append(item)

print(lista_str , lista_int)
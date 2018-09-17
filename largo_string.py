

lista_string=["ahola", "me llamo", "raul"]
largo_string=[]

for indice in lista_string:
    i = 0
    for numero in indice:
        i += 1
    largo_string.append(i)

print(largo_string)
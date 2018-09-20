
def even_number(lista):
    pares=[]
    for i in lista:
        if i % 2==0:
            pares.append(i)
    return pares

lista_numeros=[2, 4, 5,6 ,7 ,8546, 67, 8, 54, 3,45]

print(even_number(lista_numeros))
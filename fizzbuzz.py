

numeros=[1, 2, 3, 4, 5, 6 ,7 ,8 ,9, 10, 11, 12, 13, 30, 40, 60, 90, 53]

for indice in range(len(numeros)):
    numero=numeros[indice]

    if numero % 3==0 or numero % 5==0:
        valor = ""
        if numero % 3 ==0:
            valor +="Fizz"
        if numero % 5 ==0:
            valor +="Buzz"
        if numero % 3==0 and numero % 5== 0:
            valor = "Bazinga"

        if valor != "":
            numero=valor

    numeros[indice]=numero

print(numeros)
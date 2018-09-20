

lista=[10,34,545,76,45,23,30,23,5,8,90,70]
multiplos_dos=[]
multiplos_tres=[]
multiplos_cinco=[]
multiplos_siete=[]
for i in lista:
    if i % 2 == 0:
        multiplos_dos.append(i)
    if i % 3 == 0:
        multiplos_tres.append(i)
    if i % 5 == 0:
        multiplos_cinco.append(i)
    if i % 7 == 0:
        multiplos_siete.append(i)

print("Los multiplos de 2 son: {} \nLos multiplos de 3 son: {} \n"
      "Los multiplos de 5 son: {} \nLos multiplos de 7 son: {} "
      . format(multiplos_dos, multiplos_tres, multiplos_cinco, multiplos_siete))
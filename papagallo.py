

number_to_guess= 4
chance=1
user_number=int(input("Dime un numero: "))

if number_to_guess==user_number:
    print("Has ganado")
elif chance < 5:
    print("Vuelve a intentarlo")
    user_number = int(input("Dime un numero: "))
for i in range(6):
    numero = int(input(f"Digite o {i+1}º número: "))

    if numero > 0:
            print(f"O número {numero} é positivo.")
    elif numero < 0:
            print(f"O número {numero} é negativo.")
    else:
            print(f"O número {numero} é zero.")

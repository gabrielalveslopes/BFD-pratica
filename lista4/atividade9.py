import random 

numeros = random.randint(1, 20)

while True:
    chute = int(input("Digite um número entre 1 e 20: "))
    if chute < numeros:
        print("Tente um número maior.")
    elif chute > numeros:
        print("Tente um número menor.")
    else:
        print("Parabéns! Você acertou o número.")
        break
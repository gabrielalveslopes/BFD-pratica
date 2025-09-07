soma = 0

while True:
    numero = int(input("Digite um número: "))
    if numero > 0:
        soma += numero
    else:
        print(f"A soma dos números positivos é: {soma}")
        break

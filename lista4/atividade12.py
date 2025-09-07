n = int(input("Digite um número inteiro positivo: "))

for numero in range(2, n+1):
    primo = True 
    for i in range(2, numero):
        if numero % i == 0: 
            primo = False
            break
    if primo:
        print(numero)
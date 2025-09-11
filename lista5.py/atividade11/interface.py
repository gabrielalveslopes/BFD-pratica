def menu():
    print("===== Calculadora =====")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("0. Sair")
    return int(input("Escolha uma opção: "))

def ler_numeros():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    return a, b

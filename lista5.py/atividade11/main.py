import calculadora
import interface

def main():
    while True:
        opcao = interface.menu()
        if opcao == 0:
            print("Saindo...")
            break
        elif opcao in [1, 2, 3, 4]:
            a, b = interface.ler_numeros()
            operacoes = {1: "soma", 2: "subtracao", 3: "multiplicacao", 4: "divisao"}
            operacao = operacoes[opcao]
            resultado = calculadora.calculadora(a, b, operacao)
            print(f"Resultado: {resultado}")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()  

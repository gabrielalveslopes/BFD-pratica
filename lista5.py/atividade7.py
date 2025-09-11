def calculadora(a,b,operacao):
    if operacao == "soma":
        return a + b
    elif operacao == "subtração":
        return a - b
    elif operacao == "multiplicação":
        return a * b
    elif operacao == "divisão":
        return a / b
    

print(calculadora(4,5,'soma'))
print(calculadora(4,5,'multiplicação'))
print(calculadora(5,4,'subtração'))
print(calculadora(4,5,'divisão'))

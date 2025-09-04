altura = float(input("Digite a altura em metros: "))
peso = float(input("Digite o peso em kg: "))
IMC = peso / (altura * altura)
print(IMC >= 18.5 and IMC <= 24.9)

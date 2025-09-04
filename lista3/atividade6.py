idade = int(input("Digite sua idade: "))
carteira = bool(input("Possui carteira de trabalho? (sim/não): ")) == "sim"
print(idade >= 18 and carteira)
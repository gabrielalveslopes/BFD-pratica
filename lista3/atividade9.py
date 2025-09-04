produto = int(input('digite a quantidade do produto: '))
essencial = bool(input("O produto é essencial? (sim/não): ")) == "sim"
print(produto > 10 and essencial)

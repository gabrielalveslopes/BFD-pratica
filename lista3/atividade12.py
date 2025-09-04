idade = int(input("Digite a idade: "))
autorizaçao = input("Autoriza a entrada? (sim/não): ") == "sim"

print(idade >= 18 or autorizaçao)

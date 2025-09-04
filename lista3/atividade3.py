nota = float(input("Digite a nota do aluno: ")) 
trabalho = bool(input("O aluno entregou o trabalho? (sim/não): ")) == "sim"

print(nota >= 7.0 and trabalho)
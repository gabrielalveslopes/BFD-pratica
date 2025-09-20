class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
        return self.salario 
    
class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus

    def calcular_bonus(self):
        return self.salario  + self.bonus
    

class Vendedor(Funcionario):
    def __init__(self, nome, salario, comissao, vendas):
        super().__init__(nome, salario)
        self.comissao = comissao
        self.vendas = vendas

    def calcular_bonus(self):
        return self.salario + (self.vendas * self.comissao)
    

Gerente1 = Gerente("Carlos", 8000, 1000)
Vendedor1 = Vendedor("Beatriz", 4000, 5, 200)
print(f"Bonus do gerente {Gerente1.nome}: R$ {Gerente1.calcular_bonus()}")
print(f"Bonus do vendedor {Vendedor1.nome}: R$ {Vendedor1.calcular_bonus()}")
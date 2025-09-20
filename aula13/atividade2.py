from abc import ABC, abstractmethod

class Funcionario(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass



class Gerente(Funcionario):
    def __init__(self, nome, salario_base, bonus):
        self.nome = nome
        self.salario_base = salario_base
        self.bonus = bonus

    def calcular_salario(self):
        return self.salario_base + self.bonus
    
class Vendedor(Funcionario):
    def __init__(self, nome, salario_base, comissao, vendas):
        self.nome = nome
        self.salario_base = salario_base
        self.comissao = comissao
        self.vendas = vendas

    def calcular_salario(self):
        return self.salario_base + (self.comissao * self.vendas)
    

gerente = Gerente("Alice", 5000, 1500)
vendedor = Vendedor("Bob", 3000, 200, 10)
print(f'Salario do gerente {gerente.nome}: R${gerente.calcular_salario():.2f}')
print(f'Salario do vendedor {vendedor.nome}: R${vendedor.calcular_salario():.2f}') 
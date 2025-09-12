class Conta:
    def __init__(self,titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")


pessoal1 = Conta("João")
pessoal1.depositar(100)
pessoal1.sacar(30)
print(pessoal1.saldo)
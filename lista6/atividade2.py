class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0 

    def acelerar(self, aceleracao=10):
        self.velocidade += aceleracao
        print(f"O {self.marca} {self.modelo} acelerou. Velocidade atual: {self.velocidade} km/h")

    def frear(self, freio=10):
        if self.velocidade - freio < 0:
            self.velocidade = 0
            print(f"O {self.marca} {self.modelo} freou. Velocidade atual: {self.velocidade} km/h")
        else:
            self.velocidade -= freio
            print(f"O {self.marca} {self.modelo} freou. Velocidade atual: {self.velocidade} km/h")

carro1 = Carro("Ferrari", "488")

carro1.acelerar(20)
carro1.acelerar(30)
carro1.frear(10)
carro1.frear(50)
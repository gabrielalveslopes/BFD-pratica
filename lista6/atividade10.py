class Motor:
    def __init__(self, potencia):
        self.potencia = potencia


class Carro:
    def __init__(self, modelo, motor):
        self.modelo = modelo
        self.motor = motor  

    def exibir_detalhes(self):
        return f"Modelo: {self.modelo}, Motor: {self.motor.potencia} CV"


motor1 = Motor(150)
carro1 = Carro("Ferrari", motor1)

print(carro1.exibir_detalhes())
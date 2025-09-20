class Veiculo:
    def __inti__(self,modelo,marca):
        self.modelo = modelo
        self.marca = marca

    def ligar(self):
        print("O veículo está ligado.")


class Carro(Veiculo):
    def __init__(self, modelo, marca):
        super().__init__(modelo, marca)
        

    def ligar(self):
        print("O carro está ligado.")

class Moto(Veiculo):
    def __init__(self, modelo, marca):
        super().__init__(modelo, marca)

    def ligar(self):
        print("A moto está ligada.")
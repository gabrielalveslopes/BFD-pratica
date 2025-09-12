class Carro:
    def __init__(self, cor, modelo):
        self.cor = cor
        self.modelo = modelo

    def exibir_dados(self):
        print(f"Modelo: {self.modelo}\nCor: {self.cor}\n")

carro1 = Carro("Fusca", "Azul")
carro1.exibir_dados()
carro1.cor = "Vermelho"
carro1.exibir_dados()
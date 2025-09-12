class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, other):
        return Ponto(self.x + other.x, self.y + other.y)

ponto1 = Ponto(2, 3)
ponto2 = Ponto(4, 5)
print(Ponto.__str__(ponto1))
print(Ponto.__str__(ponto2))
print(Ponto.__add__(ponto1, ponto2))
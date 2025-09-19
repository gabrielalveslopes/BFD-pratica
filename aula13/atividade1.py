class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def get_preco(self):
        return self.preco
    
    def set_preco(self, novo_preco):
        if novo_preco >= 0:
            self.preco = novo_preco
        else:
            print("Preço não pode ser negativo!")

produto1 = Produto("Notebook", 2500)
produto2 = Produto("Smartphone", 1500)
print(produto1.get_preco())
print(produto2.get_preco())
produto2.set_preco(-1200) 
print(produto2.get_preco())
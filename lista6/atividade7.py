class Pedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

class Cliente:
    def __init__(self, nome):
        self.nome = nome
    

    def fazer_pedido(self, produto, quantidade):
        pedido = Pedido(produto, quantidade)
        return pedido
    
cliente1 = Cliente("João")
produto1 = Pedido("Notebook", 5)
print(f"Produto: {produto1.produto}, Quantidade: {produto1.quantidade}")
pedido1 = cliente1.fazer_pedido("Notebook", 2)
print(f"Produto: {pedido1.produto}, Quantidade: {pedido1.quantidade}")

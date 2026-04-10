class Produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    def get_nome(self): return self.__nome
    def get_quantidade(self): return self.__quantidade
    def set_quantidade(self, valor): self.__quantidade = valor
    
    def __str__(self):
        return f"Produto: {self.__nome} | Preço: R${self.__preco:.2f} | Qtd: {self.__quantidade}"

class Estoque:
    def __init__(self):
        self.produtos = []

    def cadastrar_produto(self, produto):
        self.produtos.append(produto)

    def adicionar_quantidade(self, nome, qtd):
        for p in self.produtos:
            if p.get_nome() == nome:
                p.set_quantidade(p.get_quantidade() + qtd)
                return print("Estoque atualizado!")
        print("Produto não encontrado.")

    def remover_quantidade(self, nome, qtd):
        for p in self.produtos:
            if p.get_nome() == nome:
                if p.get_quantidade() >= qtd:
                    p.set_quantidade(p.get_quantidade() - qtd)
                    return print("Retirada realizada!")
                return print("Estoque insuficiente.")
        print("Produto não encontrado.")

    def listar_produtos(self):
        for p in self.produtos: print(p)

# Implementação do Menu similar ao anterior...
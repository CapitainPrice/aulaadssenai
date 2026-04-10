class Pessoa:
    def __init__(self, nome=None, idade=None): #construtora
        if nome is None:
            nome = input("Digite seu nome: ")
        if idade is None: 
            idade = int(input("Digite sua idade: "))
        self.nome = nome 
        self.idade = idade
    def apresentar(self):
        print("Olá", self.nome)
        print("Você tem:", self.idade, "anos")

pessoa1 = Pessoa("João", 30)
pessoa1.apresentar()
aluna = Pessoa("Ana", 21)
aluna.apresentar()

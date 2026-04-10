class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print("Deposito de R$", valor, "efetuado")
        else:
            print("Valor invalido para deposito")
    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
                print("Saque de R$", valor, "efetuado")
            else:
                print("Saldo insuficiente para o saque")
        else:
            print("Valor de saque incorreto.")
    def mostrar_saldo(self):
        status = "Devendo ao banco." if self.__saldo < 0 else "Em dia"
        print("Saldo R$", self.__saldo, "-", status)
    def get_titular(self):
        return self.__titular
    def get_saldo(self):
        return self.__saldo

class Banco:
    def __init__(self):
        self.correntistas = []
    def abrir_conta(self):
        nome = input("Digite o nome do titular: ")
        conta = ContaBancaria(nome)
        self.correntistas.append(conta)
        print("Conta aberta com sucesso!")
    def encontrar_conta(self, nome):
        for conta in self.correntistas:
            if conta.get_titular() == nome:
                return conta
        return None
    def depositar_fundos(self):
        nome = input("Digite o nome do titular: ")
        conta = self.encontrar_conta(nome)
        if conta:
            try:
                valor = float(input("Digite o deposito: "))
                conta.depositar(valor)
            except ValueError:
                print("Entrada invalida")
        else:
            print("Correntista nao encontrado.")
    def sacar_fundos(self):
        nome = input("Digite o nome do titular: ")
        conta = self.encontrar_conta(nome)
        if conta:
            try:
                valor = float(input("Digite o valor de saque: "))
                conta.sacar(valor)
            except ValueError:
                print("Entrada invalida.")
        else:
            print("Correntista nao encontrado.")
    def mostrar_saldo_correntista(self):
        nome = input("Digite o nome do titular: ")
        conta = self.encontrar_conta(nome)
        if conta:
            conta.mostrar_saldo()
        else:
            print("Correntista nao encontrado.")
    def listar_contas(self):
        if not self.correntistas:
            print("Nenhuma conta cadastrada.")
            return
        print("Lista de correntistas:")
        for conta in self.correntistas:
            print("Titular:", conta.get_titular(), "- Saldo: R$", conta.get_saldo())

def main():
    banco = Banco()
    while True:
        print("\n--- Menu Bancario ---")
        print("1. Abrir conta")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Mostrar saldo")
        print("5. Listar Correntistas")
        print("6. Sair")
        opcao = input("Escolha uma opcao: ")
        if opcao == '1':
            banco.abrir_conta()
        elif opcao == '2':
            banco.depositar_fundos()
        elif opcao == '3':
            banco.sacar_fundos()
        elif opcao == '4':
            banco.mostrar_saldo_correntista()
        elif opcao == '5':
            banco.listar_contas()
        elif opcao == '6':
            print("Encerrando o sistema Bancario.")
            print("Ate logo =D")
            break
        else:
            print("Opcao invalida. Tente novamente.")

main()
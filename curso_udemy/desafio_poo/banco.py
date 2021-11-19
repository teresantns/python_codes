class Banco:
    def __init__(self):
        self.agencias = [1111, 2222, 3333]
        self.clientes = []
        self.contas = []

    def inserir_cliente(self, cliente):
        if cliente.conta is None:
            print(f'Não podemos adicionar o cliente {cliente.nome}, pois ele não tem uma conta')
            print()
            return

        self.clientes.append(cliente)
        print(f'Cliente {cliente.nome} inserido')
        print()

    def inserir_conta(self, conta):
        self.contas.append(conta)

    def autenticar(self, cliente):
        if cliente not in self.clientes:
            print(f'O cliente {cliente.nome} não é desse banco')
            print()
            return False

        if cliente.conta not in self.contas:
            print(f'A conta de número {cliente.conta.numero} do cliente {cliente.nome} não é desse banco')
            print()
            return False

        if cliente.conta.agencia not in self.agencias:
            print(f'A agência {cliente.conta.agencia} do cliente {cliente.nome} não é desse banco')
            print()
            return False

        return True

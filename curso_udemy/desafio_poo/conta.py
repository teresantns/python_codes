from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, numero, saldo):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo

    def detalhes(self):
        print(f'\033[;1mAgência: \033[0;0m', end='  ')
        print(f'{self.agencia}', end='  -  ')
        print(f'\033[;1m Número da Conta: \033[0;0m', end='  ')
        print(f'{self.numero}', end='  -  ')
        if self.saldo < 0:
            print(f'Saldo atual: \033[31m{self.saldo} \033[33m')
        else:
            print(f'Saldo atual: \033[32m{self.saldo} \033[33m')
        print('\033[0;0m')

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor do depósito precisa ser numérico")

        self.saldo += valor
        print(f'Depósito de {valor} realizado')
        self.detalhes()

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaCorrente(Conta):
    def __init__(self, agencia, numero, saldo, limite=100):
        super().__init__(agencia, numero, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('\033[31mSaldo insuficiente para esse valor de saque')
            print('\033[0;0m')
            return

        self.saldo -= valor
        print(f'Saque de {valor} realizado')
        self.detalhes()


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('\033[31mSaldo insuficiente para esse valor de saque')
            print('\033[0;0m')
            return

        self.saldo -= valor
        print(f'Saque de {valor} realizado')
        self.detalhes()

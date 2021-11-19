"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco
tem clientes e contas.

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
"""
from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca
from banco import Banco

p1 = Cliente('Teresa', 22)
p2 = Cliente('Raphaela', 22)
p3 = Cliente('Elton', 55)
p4 = Cliente('Amora', 1)

c1 = ContaPoupanca(1111, 2222, 0)
c2 = ContaCorrente(4444, 7855, 600)
c3 = ContaCorrente(2222, 85446, 5000)

p1.inserir_conta(c1)
p2.inserir_conta(c2)
p3.inserir_conta(c3)

b1 = Banco()
b1.inserir_cliente(p1)
b1.inserir_cliente(p2)
b1.inserir_cliente(p3)
b1.inserir_cliente(p4)

b1.inserir_conta(c1)
b1.inserir_conta(c2)

for cliente in b1.clientes:
    if b1.autenticar(cliente):
        print(f'Cliente {cliente.nome} autenticado - pode realizar saques')
        print()
    else:
        pass

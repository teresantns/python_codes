class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self.idade = idade
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self,  valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Idade precisa ser numérica')
        
        self._idade = valor
    

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None
    
    def inserir_conta(self, conta):
        self.conta = conta

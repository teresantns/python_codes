"""
Criar variáveis para nome (str), idade (int),
altura (float) e peso (float) de uma pessoa
Criar variável com o ano atual (int)
Obter o ano de nascimento da pessoa
Obter o IMC da pessoa com 2 casas decimais
Exibir um texto com todos os calores na tela usando F-Strings (com as chaves)
"""

nome = 'Damiano'
altura = 1.8
peso = 75
idade = 22
ano_atual = 2021

imc = peso / (altura**2)
ano_nas = ano_atual - idade

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kgs.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {ano_nas}.')


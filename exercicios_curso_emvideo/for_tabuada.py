"""
Faça um programa que mostre na tela a tabuada de um número que o usuário escolher
"""
num = int(input("Digite o número que você deseja saber a tabuada: "))
for i in range(1, 11):
    print(f'{num} x {i} = {num * i}')

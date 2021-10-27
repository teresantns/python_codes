"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. (COM FOR)
"""
num = int(input("Digite um número: "))
mult = 0

for count in range(1, num + 1):
    if num % count == 0:
        print(f'\033[39m{count}', end=' ')
        mult += 1
    else:
        print(f'\033[31m{count}', end=' ')

print()
if mult == 2:
    print(f'O número {num} é primo!')
else:
    print(f'O número {num} tem {mult} divisores, e NÃO é primo')

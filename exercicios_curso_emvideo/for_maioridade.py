"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""
from datetime import date
maiores = []
menores = []
for i in range(1, 8):
    ano = int(input(f"Digite o ano de nascimento da {i}ª pessoa: "))
    if date.today().year - ano >= 18:
        maiores.append(ano)
    else:
        menores.append(ano)

print(f'Temos {len(menores)} pessoas menores de idade')
print(f'E temos {len(maiores)} pessoas maiores de idade.')

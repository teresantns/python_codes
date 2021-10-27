"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo,
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""
# ------ minha tentativa ------------------------------------------------------
soma_idades = 0
mulheres_20 = 0
homem_velho = ''
idade_homem = 0

for i in range(1, 5):
    print(f'----- {i}ª PESSOA -----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()

    soma_idades += idade
    if sexo == 'F' and idade < 20:
        mulheres_20 += 1

    if sexo == 'M' and idade > idade_homem:
        homem_velho = nome
        idade_homem = idade

    print()

media = soma_idades / 4

print(f'A média de idade do grupo é de 29.5 anos.')
print(f'O homem mais velho tem {idade_homem} anos e se chama {homem_velho}')
print(f'Ao todo temos {mulheres_20} mulheres com menos de 20 anos')


# --------- correção professor --------------------------------------------------
"""
colocar .strip() no nome
em vez de usar o upper() pode usar sexo in 'Mm'
"""

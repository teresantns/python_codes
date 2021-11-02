
perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {'a': '1', 'b': '4', 'c': '5', },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3*2? ',
        'respostas': {'a': '4', 'b': '10', 'c': '6', },
        'resposta_certa': 'c',
    },
}

print()

respostas_certas = 0
for pk, pv in perguntas.items():  # acessando as chaves (pergunta 1, pergunta 2) e os valores
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():  # 'respostas' tem um dicionário, estamos acessando ele
        print(f'[{rk}]: {rv}')

    resposta_user = input('Qual a resposta? ')

    if resposta_user == pv['resposta_certa']:
        print("Você acertou!!")
        respostas_certas += 1
    else:
        print("Você errou...")

    print()

qtd_perguntas = len(perguntas)
porc = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi de {porc}%.')

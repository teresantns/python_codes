"""
fazer um joguinho de forca interativo com o
terminal, usando listas, fatiamento,
e as funções de listas:
append, insert, pop, del, clear, extend, +
"""

palavra = "perpendicular"  # palavra a ser adivinhada
digitadas = []  # lista com as letras digitadas pelo usuário
chances = 3  # quantas chances o usuário tem para adivinhar

"""
Se digitar uma letra certa, mostrar onde está essa letra na palavra
Se digitar uma letra errada, avisar e tirar uma chance
Se digitar um caractere inválido ou mais de uma letra, avisar 
Fechar o programa se a pessoa acertar
"""

while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break

    letra = input("Favor digitar uma letra: ")

    if letra.isdigit():
        print("Por favor digite somente letras")
        continue

    if len(letra) > 1:
        print("Por favor adivinhe uma letra de cada vez")
        continue  # mandando voltar pro início no while

    digitadas.append(letra)  # adicionando a letra adivinhada à lista

    if letra in palavra:
        print(f'A letra {letra} está na palavra! Parabéns!')
    else:
        chances -= 1
        print(f'A letra {letra} não está na palavra! Agora você tem {chances} chances...')
        digitadas.pop()  # retirando a letra da lista, para ficarmos só com as que existem na palavra

    palavra_tmp = ''  # Criando uma variável temporária para mostrarmos para o usuário como está sua adivinhação

    for letra_tmp in palavra:  # para cada letra na palavra
        if letra_tmp in digitadas:  # se o usuário adivinhou ela
            palavra_tmp += letra_tmp  # colocar no tmp
        else:
            palavra_tmp += '*'  # senão, colocar um asterisco

    if palavra_tmp == palavra:
        print(f'Você ganhou, parabéns! A palavra era {palavra_tmp}!')
        break
    else:
        print(f'A palavra adivinhada está assim: {palavra_tmp}')
        print()

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num_digitado = input("Olá! Digite um número inteiro: ")

if not num_digitado.isdigit():
    print("O número digitado não é INTEIRO!")
else:
    num_digitado = int(num_digitado)

    if num_digitado % 2 == 0:
        print(f'{num_digitado} é par')
    else:
        print(f'{num_digitado} é ímpar')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input("Que horas são? (formato de 0-23) ")

if hora.isdigit():
    hora = int(hora)

    if hora < 0 or hora > 23:
        print("Favor digitar uma hora de 0 a 23!")
    else:
        if hora <= 11:
            print("Bom dia!")
        elif hora <= 17:
            print("Boa tarde!")
        else:
            print("Boa noite!")
else:
    print("Favor digitar um horário válido (entre 0-23)!")



"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Qual o seu nome? ")
tamanho = len(nome)

if tamanho <= 4:
    print("Seu nome é curto!")
elif tamanho <= 6:
    print("Seu nome é normal!")
else:
    print("Seu nome é muito grande!")


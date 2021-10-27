"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome.
(com o print)
"""


def greetings(greet='Hello', name='User'):
    """
    This function prints a greeting in the terminal
    :param greet: str
    :param name: str
    :return: None
    """
    print(f'{greet}, {name}!')


"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre 
eles. (com o print)
"""


def summing(n1, n2, n3):
    print(f'The sum of the numbers is: {n1 + n2 + n3}')


"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""


def percentage(num, perc):
    """
    This function takes a number (num) and calculates the ércentual gain (perc) of that number
    :param num: int/float
    :param perc: int/float
    :return: float
    """
    return f'{perc}% of {num} is {num * (perc/100)} and the percentage gain is {num + num * (perc/100)}'


"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.
"""


def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 5 == 0:
        return 'buzz'
    elif num % 5 == 0:
        return 'fizz'
    else:
        return num


def argumentos(*args, **kwargs):  # posso colocar argumentos depois de definir a função
    print(args)
    print(kwargs)
    # args - argumentos / kwargs - argumentos nomeados


lista = [1, 2, 3, 4]
argumentos(*lista, nome='Teresa', sobrenome='antunes')  # tem que desempacotar a lista


"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada.
"""


def ola_mundo():
    return 'Hello World'


def mestre(funcao):
    return funcao()


print(mestre(ola_mundo))


"""
2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada. Faça a função1 executar duas funções que recebam um número 
diferente de argumentos.
"""


def diz_oi(nome):
    return f'oi {nome}'


def saudacao(sauda, nome):
    return f'{sauda} {nome}'


def mestre2(funcao, *args, **kwargs):  # função que repassa argumentos e funções!
    return funcao(*args, **kwargs)


executando = mestre2(saudacao, 'colé', 'Luiz')
print(executando)


# --------------------------------------------------------------------------
# expressões lambdas -- funções anônimas
a = lambda x, y: x * y
print(a(2, 2))

lista2 = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]
# Ordenando essa lista com o segundo elemento das listas
# lista2.sort(key=lambda item: item[1])  # desse jeito modifica a lista original
print(sorted(lista2, key=lambda i: i[1]))  # desse jeito não altera a função original
print(lista2)

# --------------------------------------------------------------------------


def main():
    greetings('Hello', 'Victoria')
    greetings()
    summing(-1, 4.6, 5)
    per = percentage(652, 0.1)
    print(per)
    fb = fizzbuzz(68)
    print(fb)


main()

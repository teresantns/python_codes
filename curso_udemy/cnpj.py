"""
Algoritmo de validação:
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0
"""
import re

MULTIPLICADORES = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def retira_caracteres(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def is_sequencia(cnpj):
    if cnpj == cnpj[0] * len(cnpj):
        return True
    else:
        return False


def calcula_digito(cnpj, digito):
    if digito == 1:
        multiplicadores = MULTIPLICADORES[1:]
        novo_cnpj = cnpj[:-2]
    elif digito == 2:
        multiplicadores = MULTIPLICADORES
        novo_cnpj = cnpj
    else:
        return None

    total = 0
    for indice, multiplicador in enumerate(multiplicadores):
        total += int(cnpj[indice]) * multiplicador

    digito = 11 - (total % 11)
    digito = digito if digito <= 9 else 0

    return f'{novo_cnpj}{digito}'


def valida_cpnj(cnpj):
    cnpj = retira_caracteres(cnpj)

    try:
        if is_sequencia(cnpj):
            return False
    except Exception:
        return False

    novo_cnpj = calcula_digito(cnpj, 1)
    novo_cnpj = calcula_digito(novo_cnpj, 2)

    if novo_cnpj == cnpj:
        return True
    else:
        return False


cnpj1 = '04.252.011/0001-10'
cnpj2 = '40.688.134/0001-61'
if valida_cpnj(cnpj2):
    print(f"CNPJ {cnpj2} é válido")
else:
    print("CNPJ Inválido")

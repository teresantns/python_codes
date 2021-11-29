"""
Programa para gerar um cpf válido
"""


def gera_cpf():
    """
    Gera um cpf aleatório válido
    :return: cpf_novo (str)
    """
    from random import randint
    numero = str(randint(100000000, 999999999))
    novo_cpf = numero  # variável que vamos criar para conferir o cpf (tirando os dois últimos digitos)
    cpf_lista = [int(i) for i in novo_cpf]

    maxs = 10
    while True:
        soma = 0
        for n, r in enumerate(range(maxs, 1, -1)):
            soma += r * cpf_lista[n]

        d = 0 if (11 - (soma % 11)) > 9 else (11 - (soma % 11))

        novo_cpf += str(d)  # colocando o digito novo no cpf
        cpf_lista.append(d)  # colocando o digito na lista do cpf
        if len(novo_cpf) < 11:
            maxs += 1  # aumentando o range do for para 11
            continue
        return novo_cpf

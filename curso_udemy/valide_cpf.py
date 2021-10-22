"""
Algoritomo para calcular os dois últimos digitos do cpf:

CPF = 168.995.350-09
------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
"""

# ---------------------- minha solução ----
cpf = str(input("Por favor digite o CPF"))
novo_cpf = cpf[:-2]  # variável que vamos criar para conferir o cpf (tirando os dois últimos digitos)
cpf_lista = [int(i) for i in novo_cpf]

maxs = 10
while True:
    if cpf == cpf[::-1]:  # eliminando cpfs com todos os números repetidos que teoricamente são válidos
        print("Seu CPF é Invalido")
        break

    soma = 0
    for n, r in enumerate(range(maxs, 1, -1)):
        soma += r * cpf_lista[n]

    d = 0 if (11 - (soma % 11)) > 9 else (11 - (soma % 11))

    novo_cpf += str(d)  # colocando o digito novo no cpf
    cpf_lista.append(d)  # colocando o digito na lista do cpf
    maxs += 1  # aumentando o range do for para 11

    if len(novo_cpf) >= 11 and novo_cpf == cpf:
        print("Seu CPF é válido")
        break
    elif len(novo_cpf) >= 11 and novo_cpf != cpf:
        print("Seu CPF é inválido")
        print(f'Seu CPF com os dois digitos finais corretos seria: {novo_cpf}')
        break

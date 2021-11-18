from dados_map import produtos, pessoas, lista

nova_lista = map(lambda x: x * 2, lista)  # daria pra fazer com list comprehension


# print(nova_lista)  # <map object at 0x7f66cadb52b0>
# print(list(nova_lista))  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p


def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.20)
    return p


# novos_produtos = map(aumenta_preco, produtos)
# for produto in novos_produtos:
#     print(produto)

# print(list(map(aumenta_idade, pessoas)))

# --------------------- filter ---------------------

nova_lista2 = filter(lambda x: x > 5, lista)
# print(list(nova_lista2))

produtos_caros = filter(lambda p: p['preco'] > 50, produtos)
print(list(produtos_caros))

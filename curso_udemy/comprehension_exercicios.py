"""
pegar a string string = '0123456789012345678901234567890123456789012345678901234567890123456789'
e transformar na lista: lista = [0123456789, 0123456789 , 0123456789, 0123456789, 0123456789, 0123456789]
e o retorno: retorno: '0123456789.0123456789.0123456789.0123456789.0123456789.0123456789'
com list comprehesion
"""
string = '0123456789012345678901234567890123456789012345678901234567890123456789'
lista = [string[i:i+10] for i in range(0, len(string), 10)]
retorno = '.'.join(lista)


"""
Fazer a soma do preço total dos produtos do carrinho abaixo com list comprehension
os itens do carrinho são descritos pelas tuplas ('produto', preço)
"""
carrinho = [('Produto 1', 30), ('Produto 2', 20), ('Produto 3', 50)]

total = sum([preco for produto, preco in carrinho])
print(total)

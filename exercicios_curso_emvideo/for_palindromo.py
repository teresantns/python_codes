"""
 Crie um programa que leia uma frase qualquer e diga se
 ela é um palíndromo, desconsiderando os espaços.
"""
frase = input("Digite uma frase: ").strip().upper()
palavras = frase.split()
juntado = ''.join(palavras)
# inverso = ''

# for letra in range(len(juntado) - 1, -1, -1):
#     inverso += juntado[letra]

# ou usando fatiamento:
inverso = juntado[::-1]

print(f'O inverso de {juntado} é {inverso}')
if inverso == juntado:
    print("Você digitou um palíndromo")
else:
    print('A frase digitada não é um palíndromo')

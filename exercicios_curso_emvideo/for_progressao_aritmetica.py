"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""
print("*-" * 34)
print("Vamos calcular os 10 primeiros termos de uma progressão aritmética?")
print("*-" * 34)
print()

term = int(input("Informe o primeiro termo da progressão: "))
ratio = int(input("Informe a razão da progressão: "))
decimo = term + (10 - 1)*ratio

for i in range(term, decimo + ratio , ratio):
    print(i, end=' -> ')
print('FIM!')

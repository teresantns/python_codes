""""
Algumas coisisnhas bestas pra treinar algumas funções
de strings e treinar formatação
"""


# ------------------------------------------------------------------ sorteando um aluno e ordem da lista
import random
lista_alunos = ['teresa', 'milena', 'luisa', 'lotus']
escolhido = random.choice(lista_alunos)
print(f'o aluno escolhido foi {escolhido}')
oop = random.sample(lista_alunos, 4)
print(oop)


# -------------------------------------------------------------- verificando primeira palavra de uma cidade
cidade = input("Em que cidade que você nasceu?").strip()
print(cidade[:5].upper() == 'SANTO')


# -------------------------- quantas vezes aparece a letra a, qual a primeira e ultima vez que aparece
frase = str(input('Digite uma frase:')).upper().strip()
count = frase.count('A')
pos1 = frase.find('A') + 1
pos2 = frase.rfind('A') + 1

print(f'A letra a aparece vezes {count}')
print(f'A letra a aparece pela primeira vez na posição {pos1}')
print(f'A letra a aparece pela última vez na posição {pos2}')

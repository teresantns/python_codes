"""
Criar dois contadores, que no mesmo laço
(ou for ou while) um conte de 0-8
e o outro conte ao contrário (10-2)
"""

for n in range(10):
    cont_1 = n
    cont_2 = 10 - n
    print(cont_1, cont_2)

# resposta professor
for p, r in enumerate(range(10, 1, -1)):
    print(p,r)

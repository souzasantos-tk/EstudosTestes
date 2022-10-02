Pes_Maior= 0
Pes_menor= 0
pesos = []

for i in range (1, 6):
    peso= float(input(f'Digite seu {i} peso:'))
    pesos.append(peso)
    print(pesos)
Pes_Maior = max(pesos)
Pes_menor = min(pesos)
print(f'O menor kg é{Pes_menor}')
print(f'O maior kg é{Pes_Maior}')
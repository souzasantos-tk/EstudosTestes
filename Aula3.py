
a = int(input('Primeiro Valor: '))
b = int(input('Segundo Valor: '))
c = int(input('Terceiro Valor: '))

if a>b and a>c:
    print('O maior numero é A: '+str(a))
elif b>a and b>c:
    print('O maior numero é B: '+str(b))
else:
    print('O maior numero é C: '+str(c))
print('Fim do Programa.')
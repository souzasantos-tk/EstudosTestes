a= int(input('Digite o Valor: '))
b= int(input('Digite o Valor: '))
print(type(a))
soma= a + b
subtracao= a - b
multiplicacao= a * b
divisao= a / b
resto= a % b
resultado=(('Soma:%i '%soma) + ('\nSubtração:%i '%subtracao)+
           ('\nMultiplicação:%d '%multiplicacao) + ('\nDivisão:%f '%divisao)+
           ('\nResto:%d '%resto))
print(resultado)

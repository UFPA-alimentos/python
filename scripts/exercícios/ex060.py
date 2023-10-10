'''
AULA 15

Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido
quando o número solicitado for negativo.
'''

while True:
    print('Digite um valor negativo para encerrar o programa')
    numero = int(input('Quer ver a tabuada de qual valor ? '))
    print('-' * 30)
    if numero < 0:
        break
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')
    print('-' * 30)

print('PROGRAMA ENCERRADO')

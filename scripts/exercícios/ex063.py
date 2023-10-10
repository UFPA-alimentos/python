'''
AULA 15

Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''

print('-=' * 15)
print(f'{"BANCO DO BRASIL":^30}')
print('-=' * 15)

valor = int(input('Que valor você quer sacar ? R$'))
total = valor
cedula = 50
TotalCedulas = 0
while True:
    if total >= cedula:
        total -= cedula
        TotalCedulas += 1
    else:
        if TotalCedulas > 0:
            print(f'Total de {TotalCedulas} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        TotalCedulas = 0
        if total == 0:
            break

print('-=' * 15)
print('PROGRAMA ENCERRADO!')

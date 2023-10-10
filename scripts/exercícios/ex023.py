'''
AULA 10

Crie um programa que leia um número inteiro e mostre na tela se
ele é PAR ou ÍMPAR.
'''

numero = int(input('Digite um número qualquer: '))
resultado = numero % 2

if resultado == 0:
    print(f'O número {numero} é PAR.')
else:
    print(f'O número {numero} é IMPAR.')

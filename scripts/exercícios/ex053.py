'''
AULA 14

Faça um programa que leia um número qualquer e mostre o seu fatorial.
'''

'''
CALCULANDO FATORIAL COM A BIBLIOTECA(MODULO) MATH

from math import factorial
numero = int(input('Digite um número para calcular seu fatorial: '))
fatorial = factorial(numero)
print(f'O fatorial de {numero} é {fatorial}')
'''

# CALCULANDO FATORIAL SEM A BIBLIOTECA(MODULO) MATH

numero = int(input('Digite um número para calcular seu fatorial: '))
contador = numero
fatorial = 1
print(f'Calculando {numero}! = ', end='')
while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
print(f'{fatorial}')

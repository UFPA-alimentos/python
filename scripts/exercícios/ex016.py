'''
AULA 08

Crie um programa que leia um número Real qualquer pelo teclado e
mostre na tela a sua porção inteira.
Ex: Digite um número: 6.127
O número 6.127 tem a parte inteira 6.
'''

from math import trunc
numero = float(input('Digite um número: '))
print(f'O número {numero} em inteiro é igual a {trunc(numero)}')

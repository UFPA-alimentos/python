'''
AULA 13

Faça um programa que leia um número inteiro e diga se
ele é ou não um número primo.
'''

numero = int(input('Digite um número inteiro: '))
total = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(i, end=' ')
print(f'\n\033[mO número {numero} foi divisível {total} vezes.')
if total == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')

'''
AULA 10

Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
'''

from datetime import date

print('obs: coloque 0 para analisar o ano atual')
ano = int(input('Qual ano você quer analisar? '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} não é BISSEXTO.')

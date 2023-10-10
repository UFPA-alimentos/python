'''
AULA 06

Faça um programa que leia algo pelo teclado e mostre na tela o seu
tipo primitivo e todas as informações possíveis sobre ele.
'''

valor = input('Digiti algo: ')
print('O tipo primitivo do valor é',type(valor))
print('Só tem espaços?',valor.isspace())
print('É um número?',valor.isnumeric())
print('É alfabetico?',valor.isalpha())
print('É alfanumerico?',valor.isalnum())
print('Esta em maisúcula?',valor.isupper())
print('Esta em minúscula?',valor.islower())
print('Esta capitalizada?',valor.istitle())

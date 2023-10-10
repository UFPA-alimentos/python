'''
AULA 12

Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
-> O primeiro valor é maior
-> O segundo valor é maior
-> Não existe valor maior, os dois valores são iguais
'''

PrimeiroNumero = int(input('Primeiro número: '))
SegundoNumero = int(input('Sengundo número: '))
if PrimeiroNumero > SegundoNumero:
    print('O PRIMEIRO número é maior')
elif SegundoNumero > PrimeiroNumero:
    print('O SEGUNDO número é maior')
else:
    print('Não existe valor maior, os dois valores são IGUAIS')

'''
AULA 08

Faça um programa que leia o comprimento do cateto oposto e do
cateto adjacente de um triângulo, calcule e mostre na tela
o comprimento da hipotenusa.
'''

from math import hypot
CatetoOposto = float(input('Comprimento do cateto oposto: '))
CatetoAdjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = hypot(CatetoOposto, CatetoAdjacente)
print(f'A hipotenusa vai medir {hipotenusa:.2f}')

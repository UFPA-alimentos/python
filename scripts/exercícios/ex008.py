'''
AULA 07

Escreva um programa que leia um valor em metros e o exiba convertido
em centímetros e milímetros.
'''

medida = float(input('Uma distâcia em metros: '))
centimetros = medida * 100
milimetros = medida * 1000
print(f'A medida de {medida:.0f}m corresponde a {centimetros:.0f}cm e {milimetros:.0f}mm')

'''
AULA 07

Faça um programa que leia a largura e a altura de uma parede em
metros, calcule a sua área e a quantidade de tinta necessária para
pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
'''

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
print(f'A sua parede tem a dimenção de {largura} x {altura} e a área de {area}m².')
tinta = area / 2
print(f'Para pintar essa parede, você precisará de {tinta:.0f}l de tinta.')

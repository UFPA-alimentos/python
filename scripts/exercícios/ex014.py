'''
AULA 07

Ecreva um programa que converta uma temperatura digitada em °C e
converta para °F.
'''

celsius = float(input('Informe a temperatura em graus celsius: '))
fahrenheit = 9 * celsius / 5 + 32
print(f'A temperatura de {celsius:.0f}ºC corresponde a {fahrenheit:.0f}ºF')

'''
AULA 13

Desenvolva um programa que leia seis números inteiros e mostre a soma
apenas daqueles que forem PARES. se o valor digitado for ímpar. Desconsidere-o.
'''

soma = 0
contador = 0
for i in range(1, 7):
    numero = int(input(f'Digite o {i}º valor: '))
    if numero % 2 == 0:
        soma += numero
        contador += 1

print(f'Você informou {contador} números PARES e a soma entre eles é igual a {soma}.')

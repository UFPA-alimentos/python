'''
AULA 10

Faça um programa que leia três números e mostre qual é o menor
e qual é o maior.
'''

PrimeiroValor = int(input('Primeiro valor: '))
SegundoValor = int(input('Sengundo valor: '))
TerceiroValor = int(input('Terceiro valor: '))
menor = PrimeiroValor

if SegundoValor < PrimeiroValor and SegundoValor < TerceiroValor:
    menor = SegundoValor
if TerceiroValor < PrimeiroValor and TerceiroValor < SegundoValor:
    menor = TerceiroValor

maior = PrimeiroValor

if SegundoValor > PrimeiroValor and SegundoValor > TerceiroValor:
    maior = SegundoValor
if TerceiroValor > PrimeiroValor and TerceiroValor > SegundoValor:
    maior = TerceiroValor
    
print(f'O Menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')

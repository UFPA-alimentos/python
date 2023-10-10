'''
AULA 14

Escreva um programa que leia um número inteiro qualquer e mostre na
tela os primeiros elementos de uma sequência de Fibonacci.
EX:
0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
'''

print('-=' * 15)
print('SEQUÊNCIA DE FIBONACCI')
print('-=' * 15)
numero = int(input('Digite quantos termos você quer mostrar: '))
PrimeiroTermo = 0
SegundoTermo = 1
print('-' * 30)
print(f'{PrimeiroTermo} -> {SegundoTermo}', end='')
contador = 1

while contador <= numero:
    TerceiroTermo = PrimeiroTermo + SegundoTermo
    print(f' -> {TerceiroTermo}', end='')
    PrimeiroTermo = SegundoTermo
    SegundoTermo = TerceiroTermo
    contador += 1

print(' -> FIM')
print('-' * 30)

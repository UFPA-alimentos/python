'''
AULA 14

Refaça o exercício 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''

print('GERADOR DE PA')
print('-=' * 10)

PrimeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = PrimeiroTermo
loop = 1

while loop <= 10:
    print(termo, end=' -> ')
    termo += razao
    loop += 1

print('FIM')

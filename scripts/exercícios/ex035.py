'''
AULA 12

Refaça o exercício 035 dos triângulos, acrescentando o recurso de
mostrar que tipo de triângulo será formado:
-> EQUILÁTERO: todos os lados iguais
-> ISÓSCELES: dois lados iguais
-> ESCALENO: todos os lados diferentes
'''

PrimeiroSegmento = float(input('Primeiro segmento: '))
SegundoSegmento = float(input('Segundo segmento: '))
TerceiroSegmento = float(input('Terceiro segmento: '))
if PrimeiroSegmento < SegundoSegmento + TerceiroSegmento and SegundoSegmento < PrimeiroSegmento + TerceiroSegmento and PrimeiroSegmento < TerceiroSegmento + SegundoSegmento:
    print('Os seguimentos acima podem formar um triângulo',end=' ')
    if PrimeiroSegmento == SegundoSegmento == TerceiroSegmento:
        print('EQUILÁTERO!')
    elif PrimeiroSegmento != SegundoSegmento != TerceiroSegmento:
        print('ESCALENO!')
    else:
        print('ISÓSCELES')
else:
    print('Os seguimentos acima NÃO podem forma um triângulo')

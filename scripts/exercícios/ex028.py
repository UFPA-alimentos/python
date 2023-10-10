'''
AULA 10

Desenvolva um programa que leia o comprimento de três retas e diga
ao usuário de elas podem ou não formar um triângulo.
'''

print('-=' * 20)
print('Analisador de Triângulo')
print('-=' * 20)
PrimeiroSegmento = float(input('Primeiro segmento: '))
SegundoSegmento = float(input('Segundo segmento: '))
TerceiroSegmento = float(input('Terceiro segmento: '))

if PrimeiroSegmento < SegundoSegmento + TerceiroSegmento and SegundoSegmento < PrimeiroSegmento + TerceiroSegmento and TerceiroSegmento < PrimeiroSegmento + SegundoSegmento:
    print('Os segmentos acima podem forma um triângulo!')
else:
    print('Os segmentos acima NÃO podem forma o triângulo')

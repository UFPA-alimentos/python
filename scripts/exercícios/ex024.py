'''
AULA 10

Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens
de até 200Km e R$0,45 para viagens mais longas.
'''

distancia = float(input('Qual é a distância da viagem? '))
print(f'Você está preste a comecar uma viagem de {distancia}km.')

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'O preço da passagem será R${preco:.2f}')

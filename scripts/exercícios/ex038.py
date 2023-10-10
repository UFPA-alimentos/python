"""
AULA 12

Crie um programa que faça o computador jogar JOKENPÔ com você.
"""
from random import randint
from time import sleep
print('''Suas opcões:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
itens = ('pedra', 'papel', 'tesoura')
OpcaoComputador = randint(0, 2)
OpcaoJogador = int(input('Qual é a sua jogada ? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)
print('-=' * 11)

print(f'Computador jogou {itens[OpcaoComputador]}')
if OpcaoJogador == 0:
    print('Você jogou pedra')
elif OpcaoJogador == 1:
    print('Você jogou papel')
elif OpcaoJogador == 2:
    print('Você jogou tesoura')
else:
    print('JOGADA INVÁLIDA !')

print('-=' * 11)

if OpcaoJogador == 0:
    if OpcaoComputador == 0:
        print('EMPATE')
    elif OpcaoComputador == 1:
        print('COMPUTADOR GANHOU')
    elif OpcaoComputador == 2:
        print('VOCÊ GANHOU')
    else:
        print('JOGADA INVÁLIDA !')
elif OpcaoJogador == 1:
    if OpcaoComputador == 0:
        print('VOCÊ GANHOU')
    elif OpcaoComputador == 1:
        print('EMPATE')
    elif OpcaoComputador == 2:
        print('COMPUTADOR GANHOU')
    else:
        print('JOGADA INVÁLIDA !')
elif OpcaoJogador == 2:
    if OpcaoComputador == 0:
        print('COMPUTADOR GANHOU')
    elif OpcaoComputador == 1:
        print('VOCÊ GANHOU')
    elif OpcaoComputador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA !')
else:
    print('JOGADA INVÁLIDA !')

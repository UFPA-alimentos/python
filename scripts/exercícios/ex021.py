'''
AULA 10

Escreva um programa que faça o computador "pensar" em um número
inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi
o número escolhido pelo computador. O programa deverá escrever na
tela se o usuário venceu ou perdeu.
'''

from random import randint
from time import sleep

NumeroComputador = randint(0, 5) # o compuatador escolhe um número, nesse caso, entre 0 e 5
print('=+='*20)
print('Vou pensar em número de 0 a 5. Tente adivinhar...')
print('=+='*20)
NumeroJogador = int(input('Em que número eu pensei? ')) #jogador escolhe um número
print('PROCESSANDO...')
sleep(3) #tempo de processamento para o resultado aparecer

if NumeroJogador == NumeroComputador:
    print('PARABÉNS! Você consequiu vencer!')
else:
    print(f'GANHEI! Eu pensei no número {NumeroComputador} e não em {NumeroJogador}')
'''
AULA 14

Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
em um número entre 0 e 10. Só que agora o jogador vai tentar
adivinhar até acertar, mostrando no final quantos palpites foram
necessários para vencer.
'''

from random import randint
print('=+=' * 10)
print(f'{"JOGO DA ADIVINHAÇÃO":^30}')
print('=+=' * 10)
print('Olá! Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi ?')
NumeroComputador = randint(0, 10)
acertou = False
tentativas = 0
while not acertou:
    PalpiteJogador = int(input('Qual é seu palpite: '))
    tentativas += 1
    if PalpiteJogador == NumeroComputador:
        acertou = True
    else:
        if PalpiteJogador < NumeroComputador:
            print('Eu pensei em número maior')
        elif PalpiteJogador > NumeroComputador:
            print('Eu pensei em número menor')
print(f'Acertou com {tentativas} tentativas. Parabéns!')

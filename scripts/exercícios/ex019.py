'''
AULA 08

Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o
nome do escolhido.
'''

from random import choice
PrimeiroNome = str(input('Primeiro aluno: '))
SegundoNome = str(input('Sengundo aluno: '))
TerceiroNome = str(input('Terceiro aluno: '))
QuartoNome = str(input('Quarto aluno: '))
lista = [PrimeiroNome, SegundoNome, TerceiroNome, QuartoNome]
NomeEscolhido = choice(lista)
print(f'O aluno escolhodo foi {NomeEscolhido}.')
 
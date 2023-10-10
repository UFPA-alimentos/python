'''
AULA 08

O mesmo professor do desafio anterior quer sortear a ordem de apresentação
de trabalhos dos alunos. Faça um programa que leia o nome dos quatros alunos
e mostre a ordem sorteada.
'''

from random import shuffle
PrimeiroNome = str(input('Primeiro aluno: '))
SegundoNome = str(input('Sengundo aluno: '))
TerceiroNome = str(input('Terceiro aluno: '))
QuartoNome = str(input('Quarto aluno: '))
lista = [PrimeiroNome, SegundoNome, TerceiroNome, QuartoNome]
shuffle(lista)
print(f'A ordem de apresentaçâo dos alunos será {lista}.')

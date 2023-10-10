'''
AULA 07

Crie um programa que leia as duas notas de um aluno, calcule e mostre a sua média
'''

PrimeiraNota = float(input('Primeira nota do aluno: '))
SegundaNota = float(input('Segunda nota do aluno: '))
media = (PrimeiraNota + SegundaNota) / 2
print(f'A média etre {PrimeiraNota:.1f} e {SegundaNota:.1f} é igual a {media:.1f}')

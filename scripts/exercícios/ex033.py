'''
AULA 12

Crie um programa que leia duas notas de um aluno e calcule a sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
-> Média abaixo de 5.0: REPROVADO
-> Média entre 5.0 e 6.9: RECUPERAÇÃO
-> Média 7.0 ou superior: APROVADO
'''

PrimeiraNota = float(input('Primeira nota: '))
SegundaNota = float(input('Segunda nota: '))
media = (PrimeiraNota + SegundaNota) / 2
print(f'Se o aluno tirou {PrimeiraNota:.1f} e {SegundaNota:.1f} a média do aluno é igual a {media:.1f}')
if media >= 5 and media < 7:
    print('O aluno está em RECUPERAÇÃO')
elif media < 5:
    print('O aluno está REPROVADO')
else:
    print('O aluno está APROVADO')

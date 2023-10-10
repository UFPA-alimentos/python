'''
AULA 12

Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade, se ele ainda vai se alistar ao servoço militar,
se é a hora de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou o tempo
que passou do prazo do alistamento militar.
'''

from datetime import date
atual = date.today().year
AnoNascimento = int(input('Ano de nascimento: '))
idade = atual - AnoNascimento
print(f'Quem nasceu em {AnoNascimento} tem {idade} anos em {atual}')
if idade == 18:
    print('Você tem que se alista IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para seu alistamento militar')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado a {saldo} anos.')

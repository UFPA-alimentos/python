'''
AULA 13

Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores de idade.
'''
from datetime import date
AnoAtual = date.today().year
MaiorIdade = 0
MenorIdade = 0
for i in range(1, 8):
    DataNascimento = int(input(f'Em que ano a {i}º pessoa nasceu ? '))
    if DataNascimento < AnoAtual - 17:
        MaiorIdade += 1
    else:
        MenorIdade += 1

print(f'Ao todo tivemos {MaiorIdade} maiores de idade')
print(f'E também tivemos {MenorIdade} pessoas menores de idade')

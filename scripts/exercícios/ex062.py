'''
AULA 15

Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
cadastrada, o programa deverá perguntar se o usuário quer ou não
continuar. No final, mostre:

A - quantas pessoas tem mais de 18 anos.
B - Quantos homens foram cadastrados.
C - Quantas mulheres tem menos de 20 anos.
'''

MaiorIdade = 0
TotalHomens = 0
TotalMulheresMenos20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    if idade >= 18:
        MaiorIdade += 1

    if sexo == 'M':
        TotalHomens += 1

    if sexo == 'F' and idade < 20:
        TotalMulheresMenos20 += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

print(f'Total de pessoas maiores de idade: {MaiorIdade}')
print(f'Ao todo temos {TotalHomens} homens cadastrados')
print(f'E temos {TotalMulheresMenos20} mulheres com menos de 20 anos')
print('ACABOU!')

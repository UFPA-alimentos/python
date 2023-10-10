'''
AULA 13

Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
'''

MenorPeso = 0
MaiorPeso = 0
for i in range(1, 6):
    peso = float(input(f'Peso da {i}º pessoa: '))
    if i == 1: # se o meu índice i for a primeira pessoa analisada
        MaiorPeso = peso
        MenorPeso = peso
    else: # se o meu índice i não for a primeira pessoa analisada
        if peso > MaiorPeso:
            MaiorPeso = peso
        if peso < MenorPeso:
            MenorPeso = peso

print(f'O menor peso lido foi de {MenorPeso}Kg')
print(f'O maior peso lido foi de {MaiorPeso}Kg')

'''
AULA 13

Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final, do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
'''

SomaIdade = 0
MediaIdade = 0
IdadeHomemMaisVelho = 0
NomeHomemMaisVelho = ''
TotalMulheres20 = 0 # variável responsavel por armazenar o número de mulheres menores de 20 anos

for i in range(1, 5):
    print(f'----- {i}º PESSOA -----')
    nome = str(input(f'Nome: ')).strip()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo (F / M): ')).strip()
    SomaIdade += idade
    if i == 1 and sexo in 'Mm':
        IdadeHomemMaisVelho = idade
        NomeHomemMaisVelho = nome
    if sexo in 'Mn' and idade > IdadeHomemMaisVelho:
        IdadeHomemMaisVelho = idade
        NomeHomemMaisVelho = nome
    if sexo in 'Ff' and idade < 20:
        TotalMulheres20 += 1

MediaIdade = SomaIdade / 4
print(f'A média de idade do grupo é de {MediaIdade} anos')
print(f'O homem mais velho tem {IdadeHomemMaisVelho} anos e se chama {NomeHomemMaisVelho}')
print(f'Ao todo são {TotalMulheres20} mulheres com menos de 20 anos')

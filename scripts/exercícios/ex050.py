'''
AULA 14

Faça um programa que leia o sexo de uma pessoa, mas só aceite
os valores 'M' ou 'F'. Caso esteja errado, peça a digitação
novamente até ter um valor correto.
'''

sexo = input('Informe seu sexo (F / M): ').strip().upper()[0]
while sexo not in 'FM':
    sexo = input('Dados Inválidos. Por favor, informe seu sexo: ').strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')

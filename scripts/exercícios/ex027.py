'''
AULA 10

Escreva um programa que pergunte o salário de um funcionário e
calcule o valor do seu aumento. Para salários superiores a R$1.250,00,
calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
'''

salario = float(input('Qual é o salario do fucionário? R$'))
if salario <= 1.250:
    novo = salario + (salario * 15 / 100) #aumento 15%
else:
    novo = salario + (salario * 10 / 100) # aumento 10%
print(f'Quem ganhava R${salario:.3f}, agora passa a ganhar R${novo:.3f}')

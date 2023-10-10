'''
AULA 07

Faça um algoritmo que leia o salário de um funcionário e mostre seu
novo salário, com 15% de aumento.
'''

salario = float(input('Quanto é o salário do fucionário R$:'))
NovoSalario = salario + (salario * 15 / 100)
print(f'O salario do fucionário que era R${salario:.3f} com o aumento de 15% vai para R${NovoSalario:.3f}')

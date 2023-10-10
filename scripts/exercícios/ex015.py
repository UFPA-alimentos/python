'''
AULA 07

Escreva um programa que pergunte a quantidade de KM percorridos
por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15
por KM rodado.
'''

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
pago = (dias * 60) + (km * 0.15)
print(f'O valor total a ser pago é de R${pago:.2f}')

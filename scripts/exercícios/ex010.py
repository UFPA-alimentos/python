'''
AULA 07

Crie um programa que leia quanto dinheiro em reais uma pessoa tem
na carteira e mostre quantos Dólares, Euros e Libras ela pode comprar.
considere a cotação atual de cada moeda.
'''

real = float(input('Quanto dinheiro voçê tem na carteira? R$'))
dolar = real / 4.87
euro = real / 5.28
libra = real / 6.15
print(f'Com R${real:.2f} você pode comprar: \nUS${dolar:.2f}  \nEU${euro:.2f} \nLI${libra:.2f}')

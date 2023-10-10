'''
AULA 12

Escreva um programa para aprovar o empréstimo bancário para a compra
de uma casa. Pergunte o valor da casa, o salário do comprador e em
quantos anos ele vai pagar.
A prestação mensal, não pode exceder 30% do seu salário ou então o
empréstimo será negado.
'''

casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = float(input('Quantos anos de finaciamento?'))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma casa de R${casa:.3f} em {anos:.0f} anos.', end=' ')
print(f' a prestação será de R${prestacao:.3f}')
if prestacao <= minimo:
    print('Emprétimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')

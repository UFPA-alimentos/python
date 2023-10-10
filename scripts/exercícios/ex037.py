"""
AULA 12
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e a condição de pagamento:
    - à vista DINHEIRO/CHEQUE: 10% de desconto
    - à vista no CARTÃO: 5% de desconto
    - em até 2x no CARTÃO: preço normal
    - 3x ou mais no CARTÃO: 20% de juros
"""

print(f'{" LOJAS UFPA ":=^40}')
PrecoCompra = float(input('Digite o preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a sua forma de pagamento ? '))

if opcao == 1:
    total = PrecoCompra - (PrecoCompra * 10 / 100)
elif opcao == 2:
    total = PrecoCompra - (PrecoCompra * 5 / 100)
elif opcao == 3:
    total = PrecoCompra
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS.')
elif opcao == 4:
    total = PrecoCompra + (PrecoCompra * 20 / 100)
    TotalParcela = int(input('Quantas parcelas ? '))
    parcela = total / TotalParcela
    print(f'Sua compra será parcelada em {TotalParcela}x de {parcela:.2f} COM JUROS.')
else:
    total = PrecoCompra
    print('Opção inválida de pagamento. Tente novamente!')
print(f'Sua compra de R${PrecoCompra:.2f} vai custar R${total:.2f} no final.')

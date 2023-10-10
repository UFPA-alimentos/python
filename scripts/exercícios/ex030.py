'''
AULA 12

Escreva um programa que leia um número inteiro qualquer e peça para
o usuário escolher qual será a base de conversão:
-> 1 para BINÁRIO
-> 2 para OCTAL
-> 3 para HEXADECIMAL
'''

numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Coverta para BINÁRIO
[ 2 ] Converta para OCTAL
[ 3 ] Converta para HEXADECIMAL''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{numero} Convertido para BINÁRIO é iqual a {bin(numero)[2:]}')
elif opcao == 2:
    print(f'{numero} Covertido para OCTAL é igual a {oct(numero)[2:]}')
elif opcao == 3:
    print(f'{numero} Covertido para HEXADECIMAL é igual a {hex(numero)[2:]}')
else:
    print('Opção inválida, tente novamente')

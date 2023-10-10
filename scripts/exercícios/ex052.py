'''
AULA 14

Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''

from time import sleep
ligado = True
PrimeiroValor = int(input('Primeiro valor: '))
SegundoValor = int(input('Segundo Valor: '))
while ligado:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('>>>>> Digite a sua opção: '))
    sleep(2)
    if opcao == 1:
        print(f'A soma entre {PrimeiroValor} e {SegundoValor} é igual a {PrimeiroValor + SegundoValor}')
        print('=+=' * 10)
    elif opcao == 2:
        print(f'A multiplicação entre {PrimeiroValor} e {SegundoValor} é igual a {PrimeiroValor * SegundoValor}')
        print('=+=' * 10)
    elif opcao == 3:
        if PrimeiroValor < SegundoValor:
            print(f'Entre {PrimeiroValor} e {SegundoValor} o maior valor é {SegundoValor}')
            print('=+=' * 10)
        elif PrimeiroValor > SegundoValor:
            print(f'Entre {PrimeiroValor} e {SegundoValor} o maior valor é {PrimeiroValor}')
            print('=+=' * 10)
        else:
            print(f'Os valores são iguais')
            print('=+=' * 10)
    elif opcao == 4:
        print('=+=' * 10)
        PrimeiroValor = int(input('Primeiro valor: '))
        SegundoValor = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Obrigado por usar o meu programa :)')
        ligado = False
    else:
        print('Opção inválida. Tente novamente')

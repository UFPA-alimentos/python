'''
AULA 14

Crie um programa que leia vários números inteiros pelo teclado. No
final da execução, mostre a média enttre todos os valores e qual foi
o maior e o menor valores lidos. O programa deve perguntar ao usuário
se ele quer ou não continuar a digitar valores.
'''

resposta = 'S'
soma = contador = media = maior = menor = 0
while resposta in 'S':
    numero = int(input('Digite um número: '))
    soma += numero
    contador += 1
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Quer continuar ? [S / N]: ')).strip().upper()[0]

media = soma / contador
print(f'Você digitou {contador} números e a média entre eles é igual a {media}')
print(f'O menor valor foi {menor} e o maior valor foi {maior}')

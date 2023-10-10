'''
AULA 12

Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
-> Abaixo de 18.5: abaixo do peso
-> Entre 18.5 e 25: peso ideal
-> 25 até 30: sobrepeso
-> 30 até 40: obesidade
-> Acima de 40: obesidade mórbida
'''

peso = float(input('Qual é seu peso? (KG): '))
altura = float(input('Qual é sua altura? (M): '))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está no PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE')
elif imc >= 40:
    print('Voê está em OBESIDADE MÓRMIDA, cuidado!')

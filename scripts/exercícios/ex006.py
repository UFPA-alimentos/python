'''
AULA 07

Crie um algoritmo que leia um número e mostre o seu dobro, triplo
e raiz quadrada.
'''

numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)
print(f'O dobro de {numero} vale {dobro}\nO triplo vale {triplo}\nAraiz quadrada é {raiz:.2f}')

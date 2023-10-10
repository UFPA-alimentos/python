'''
AULA 14

Melhore o exercício 061, perguntando para o usuário se ele quer mostrar
mais alguns termos. O programa encerra quando ele disser que
quer mostrar 0 termos.
'''

print('GERADOR DE PA')
print('-=' * 10)

PrimeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = PrimeiroTermo
loop = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while loop <= total:
        print(termo, end=' -> ')
        loop += 1
        termo += razao
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais ? '))

print(f'Progressão finalizada com {total} termos mostrados.')
print('FIM')

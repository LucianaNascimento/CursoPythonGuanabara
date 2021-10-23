''' Faça um programa que leia um número qualquer e mostre
o seu fatorial
exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120
'''

num = int(input('Digite um número para calcular seu fatorial: '))
contador = num
fatorial = 1

print(f'Calculando {num}! = ', end="")
while contador > 0:
    print(f'{contador}', end="")
    print(" x " if contador > 1 else " = ", end="")
    fatorial *= contador
    contador -= 1

print(f'{fatorial}')
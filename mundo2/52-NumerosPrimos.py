''' Faça um programa que leia um número inteiro e diga se ele é ou não
um número primo'''

num = int(input('Digite um número e descubra se um número é primo: '))

isPrime = True
current = (num // 2)

for i in range(current, 0, -1):
    if num % i == 0 and i != 1:
        isPrime = False

if isPrime:
    print(f'O número {num} é primo.')
else:
    print(f'O número {num} não é primo')

#ou

num = int(input('Digite um número e descubra se um número é primo: '))
total = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\33[33m', end='')
        total += 1
    else:
        print('\33[31m', end='')
    print(f'{c}', end=' ')
print(f'\n\33[mO número {num} foi divisível {total} vezes')
if total == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')



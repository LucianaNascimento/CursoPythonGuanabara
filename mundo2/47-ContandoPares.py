# Crie um programa que mostre na tela todos os números pares
# que estão no intervalo entre 1 e 50

for num in range(1, 51):
    if num % 2 == 0:
        print(num, end=' ')
print('Acabou')
#ou
for num in range(2, 51, 2):
        print(num, end=' ')
print('Acabou')
'''Faç um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi
o maior e menor e as suas respectivas posições na lista.'''


listaNum = []
maior = 0
menor = 0

for c in range (0, 5):
    listaNum.append(int(input(f'Digite um valor para a Posição {c+1}: ')))
    if c ==0:
        maior = menor = listaNum[c]
    else:
        if listaNum[c] > maior:
            maior=listaNum[c]
            if listaNum[c] < menor:
                menor = listaNum[c]


print('=-' * 30)
print(f'Você digitou os valores {listaNum}')
print(f'O menor valor digitado foi {menor} na posição ', end='')
for i, v in enumerate(listaNum):
    if v == menor:
        print(f'{i+1}... ', end='')
print()
print(f'O maior número digitado foi {maior} na posição ', end='' )
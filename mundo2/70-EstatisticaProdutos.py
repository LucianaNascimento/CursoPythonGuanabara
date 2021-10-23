'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
a) qual é o total gasto na compra
b) quantos produtos custam mais de R$ 1000
c) qual é o nome do produto mais barato
'''

barato = ''
total = totMil = menor = cont = 0

while True:
    produto = str(input('Nome do produto: \n'))
    preco = float(input('Preço: R$ \n'))

    cont += 1
    total += preco

    if preco > 1000:
        totMil += 1

    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] \n')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Total compra: R$ {total:.2f}')
print(f'Produtos que custam mais do que R$1.000: {totMil}')
print(f'O produto mais barato é {barato}, que custa R${menor:.2f}')

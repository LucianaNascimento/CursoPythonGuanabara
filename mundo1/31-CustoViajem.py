'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200km
e R$ 0,45 para viagens mais longas
'''

dist = int(input("Digite a distância a ser percorrida? "))
if dist <= 200:
    preco = (dist * 0.50)
    print(f"Preço da passagem: R${preco:.2f}.")
else:
    preco = (dist * 0.45)
    print(f"Preço da passagem: R$ {preco:.2f}.")
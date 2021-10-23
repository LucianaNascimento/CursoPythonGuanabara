# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input("Digite o preço de um produto: \nR$ "))
desconto = float(input('Digite o valor do desconto: '))
v_desconto = preco - (preco * desconto /100)
print(f'Preço anterior {preco:.2f}, na promoção com desconto de {desconto}%, o produto vai custar {v_desconto:.2f}')
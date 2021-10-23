'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal, e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- em 3x ou mais no cartão: 20% de juros
'''
preco = float(input("Digite o preço do produto: "))
print("Selecione uma forma de pagamento:")
print('''
Digite 1: Para pagar à vista no dinheiro.
Digite 2: Para pagar à vista no cartão.
Digite 3: Em 2x no cartão.
Digite 4: Em 3x no cartão ou mais \n''')
opcao = int(input("Selecione a forma de pagamento: \n"))

if opcao == 1:
    print("Você selecionou à vista no dinheiro.")
    total = preco - (preco * 10/100)

elif opcao == 2:
    print('Você selecionou à vista no cartão.')
    total = preco - (preco * 5/100)

elif opcao == 3:
    print('Você selecionou em 2x no cartão.')
    total = preco
    parcela = total / 2
    print(f'Duas parcelas de R$ {parcela}.')

elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print(f'Sua compra será parcelada em {totalparc}x de R${parcela} (com juros)')
else:
    total = ' XX'
    print("Por favor, selecione uma alternativa válida. Tente novamente.")
print(f'Sua compra de R$ {preco} vai custar R$ {total} no final')

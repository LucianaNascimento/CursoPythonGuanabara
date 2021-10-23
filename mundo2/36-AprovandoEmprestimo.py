'''
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa
O programa vai perguntar o valor da casa, o salário do comprador e em quantos
anos ele vai pagar
Calcule o valor da prestação mensal,
sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado
'''

casa = float(input("Qual o valor da casa? \n"))
salario = float(input("Qual é o valor do salário? \n"))
tempo = int(input("Quantos anos de financiamento? \n"))
prestacao = (casa / (tempo * 12))
minimo = salario * 30 / 100


print(f"Valor da casa: {casa:.2f}")
print(f"Prestação: {prestacao:.2f}")

if prestacao <= minimo:

    print("Empréstimo concedido.")
else:
    print('Empréstimo negado')
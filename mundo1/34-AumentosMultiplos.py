'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
Para os inferiores ou iguais, o aumento é de R$ 15%.
'''

salario = float(input("Digite o valor do salário: \n"))
if salario <= 1250:
    s_aumento = salario + (salario * 15/100)
else:
    s_aumento = salario + (salario * 10/100)
print(f'Quem ganhava R$ {salario:.2f} passa a ganhar R$ {s_aumento:.2f} agora.')
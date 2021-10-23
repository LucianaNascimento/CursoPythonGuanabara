# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario = float(input("Digite o valor do salário: \nR$ "))
aumento = float(input("Digite a porcentagem do aumento: \nR$ "))
v_aumento = salario + (salario*aumento/100)
print(f"O salário do funcionário, que é de R$ {salario:.2f}, vai subir para R$ {v_aumento:.2f} com o aumento de {aumento}%.")
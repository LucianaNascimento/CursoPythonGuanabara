# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

# ex.: digite um número: 1834
# unidade: 4
# dezenas: 3
# centenas: 8
# milhares: 1

num = int(input("Digite um número de 0 a 9999 a ser fatiado: \n"))

uni = num // 1 % 10
dez = num // 10 % 10
cent = num // 100 % 10
mil = num // 1000 % 10

print(f"Unidade: {uni}")
print(f"Dezena: {dez}")
print(f"Centena: {cent}")
print(f"Milhar: {mil}")
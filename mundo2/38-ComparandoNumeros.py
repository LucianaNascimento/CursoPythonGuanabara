'''
Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
- o primeiro valor é maior
- o segundo valor é maior
- não existe valor maior; os dois são iguais
'''

print('-=' * 20)
print("COMPARANDO NÚMEROS")
print('-=' * 20)
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

if num1 > num2:
    print("O primeiro valor é maior!")
elif num2 > num1:
    print("O segundo valor é maior")
else:
    print("Não existe valor maior, os números digitados são iguais.")
# Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e sua raiz quadrada:

num = int(input("Digite um número: \n"))

dobro = num *2
triplo = num *3
raiz = num ** (1/2)

print(f"O dobro de {num} é: {dobro}!")
print(f"O triplo de {num} é: {triplo}.")
print(f"A raiz quadrada de {num} é: {raiz:.2f}.")
'''
Crie um programa onde o usuário digite uma expressão qualquer
que use parênteses.
Seu aplicativo deverá analisar se a expressão passada
está com os parênteses abertos e fechados na ordem correta.
'''


'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares
e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''

num = []
pares = []
impares = []

while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for indice, valor in enumerate(num):
    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 == 1:
        impares.append(valor)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')



'''
ou

lista = []
pares = []
impares = []

while True:
    lista.append(int(input("Digite um número: ")))
    cont = str(input("Quer continuar? ")).strip().upper()
    if cont[0] == "S":
        print("Continuando.")
    elif cont[0] == "N":
        print("Programa finalizado.")
        break
    else:
        print("Digite uma resposta válida.")


for num in lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(f"Lista de números digitados: {lista}.")
print(f"Lista de números pares: {pares}.")
print(f"Lista de números ímpares: {impares}.")

'''
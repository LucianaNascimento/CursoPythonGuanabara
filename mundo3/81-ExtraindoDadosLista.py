'''
Crie um programa que vai ler vários números e colocá-los em uma lista
Depois disso, mostre:
a) quantos números foram digitados.
b) a lista de valores, ordenada de forma decrescente
c) se o valor 5 foi digitado e está ou não na lista.
'''


valores = []

while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer cotinuar? [S/N]' ))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem descrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista1')
else:
    print('O valor 5 não foi encontrado na lista!')



'''

ou

lista = []

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

print(f"{len(lista)} números foram digitados.")

lista.sort(reverse=True)
print(f"Esta é a lista ordenada decrescentemente {lista}")

if 5 in lista:
    print(f"O valor 5 foi digitado.")
else:
    print("O valor 5 não foi digitado.")
'''


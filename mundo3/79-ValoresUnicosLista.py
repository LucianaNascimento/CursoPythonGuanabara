'''Crie um programa que o usuário posa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores
únicos digitados, em ordem cescente.'''

numeros = list()

while True:

    n = int(input('Digite um valor: '))
    if n not  in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!!')
    else:
        print('Valor duplicado, não vou adicionar...')

    r = str(input('Quer continuar? [S/N] '))

    if r in 'Nn':
        break

print('=-' * 30)
print(f'Você adicionou os valores {numeros}')

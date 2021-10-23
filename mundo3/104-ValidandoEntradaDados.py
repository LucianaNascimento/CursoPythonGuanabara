"""
Crie um programa que tenha a função leia_int(),
que vai funcionar de forma semelhante à função input do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
ex.:
n = leia_int("Digite um n")
"""


def leia_int(texto_usuario):
    ok = False
    value = 0
    while True:
        numero = input(f'{texto_usuario} ')
        if numero.isnumeric():
            valor = numero
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido!\033[m')
        if ok:
            break
    return valor

n = leia_int('Digite um número:')
print(f'Você acabou de digitar o número: {n}.')
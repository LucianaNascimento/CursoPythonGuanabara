''' Crie um programa que leia vários números inteiros pelo teclado
O programa só vai parar quando o usuário digitar 999,
que é a condição de parada (flag).
No final, mostre quantos números foram digitados
e qual foi a acc entre eles (desconsiderando o flag)
'''
soma = contador = 0

while True:
    num = int(input('Digite um número inteiro [999 para parar]: '))
    if num == 999:
        break
    else:
        contador += 1
        soma += num
print(f'Foram digitados {contador} números e a soma entre eles foi {soma}.')

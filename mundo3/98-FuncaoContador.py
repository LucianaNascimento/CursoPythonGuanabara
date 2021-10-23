'''Faça um programa que tenha uma função chama contador(), que recebe três parametros: inicio, fim e pesso.
Seu programa tem que realizar trÊs contagens através da função criada:
a- De 1 até 10, de 1 em 1
b- De 10 até 0, de 2 em 2
c- Uma contagem personalizada'''

from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        print('Não existe passo de 0, vou fazer passo de 1 em 1')
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p } em {p}')
    sleep(1)


    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >=f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')


#programa principal
contador(1, 10, 1)
contador(10, 0, 2)

print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')

ini = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)
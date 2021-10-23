'''faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
retangular (largura e comprimento) e mostre a área do terreno.'''

def area(larg, compr):
    a = larg * compr
    print(f'A área de um terreno {larg} x {compr} é de {a:.2f} m2.')

#programa principal
print(' Controle de Terrenos ')
print('-' * 30)

l= float(input('LARGURA (m): '))
c= float(input('COMPRIMENTO (m): '))
area(l, c)
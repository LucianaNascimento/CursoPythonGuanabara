'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
from random import randint
from time import sleep
computador = randint(0, 5)

print("--=--" * 15)
print("Vou pensar em um número entre 0 e 5, tente adivinhar.")
print("--=--" * 15)
num = int(input("Em qual número você acha que eu pensei?: \n"))
print("Pensando...")
sleep(1)

if num > 5 or num < 0:
  print('O número é entre 0 e 5, vc digitou errado!')
else:
    if num == computador:
        print(f"Número digitado: {num}.")
        print("Parabéns, você venceu!")
    else:
        print(f"Número digitado: {num}.")
        print(f"Ganhei!! Eu pensei no número {computador} e não no {num}. Tente novamente.")
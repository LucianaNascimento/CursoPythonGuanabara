'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''

from random import randint
from time import sleep

itens = ["pedra", "papel", "tesoura"]
computador = randint(0, 2)

print('''
COMPUTADOR: Vamos jogar Pedra, Papel, Tesoura!
As regras são as seguintes:
- Papel vence Pedra e perde para Tesoura
- Pedra vence Tesoura e perde para Papel
- Tesoura vence Papel e perde para Pedra
- opção [0] Pedra
- opção [1] Papel
- opção [2] Tesoura \n
''')


jogador = int(input("Qual a sua opção? \n"))
print('-=' * 15)
print(f'O computador escolheu {itens[computador]}')
print(f'O jogador escolheu {itens[jogador]}')
print('-=' * 15)
print("JO")
sleep(0.5)
print("KEN")
sleep(0.5)
print("PÔ!!!")
print('-=' * 15)


if computador == 0: #computador jogou pedra
    if jogador  == 0: #pedra
        print('Empate!')
    elif jogador  == 1: #papel
        print('Você venceu!!!!')
    elif jogador == 2:  # tesoura
        print('O computador venceu!')
    else:
        print('Jogada inválida')

elif computador == 1: #computador jogou papel
    if jogador  == 0: #pedra
        print('O computador venceu!')
    elif jogador  == 1: #papel
        print('Empate!')
    elif jogador == 2:  # tesoura
        print('Você venceu!!!!')
    else:
        print('Jogada inválida')
elif computador == 2: #computador jogou tesoura
    if jogador  == 0: #pedra
        print('Você venceu!!!!')
    elif jogador  == 1: #papel
        print('O computador venceu!')
    elif jogador == 2:  # tesoura
        print('Empate!')
    else:
        print('Jogada inválida')
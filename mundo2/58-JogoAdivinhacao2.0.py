''' Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer
'''

from random import randint

computador = randint(0, 10)
print('Estou pensando em um número entre 0 e 10...')
print('Será que você consegue adivinhar? ')

acertou = False
palpites = 0


while not acertou:
    jogador = int(input('Em qual número você acha que eu pensei? '))
    palpites += 1
    if jogador == computador:  # entrada errada do usuário
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez!')
        elif jogador > computador:
            print('Menos... Tente mais uma vez!')

print(f'Acertou com {palpites} tentativas, parabéns!!')

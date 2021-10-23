"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.
"""

jogador = dict()
gols_total = 0

# Nome
jogador['nome'] = input('Qual o nome do(a) jogador(a)? ')

# Partidas
jogador['partidas'] = int(input('Partidas jogadas: '))

# Gols em cada partida
for partida in range(jogador['partidas']):
    gols_partida = int(input(f'Quantos gols o jogador {jogador["nome"]} fez na partida {partida +1}? '))
    gols_total += gols_partida
jogador['gols_total'] = gols_total


print(
    f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas e fez um total de {jogador["gols_total"]} gols.'
)
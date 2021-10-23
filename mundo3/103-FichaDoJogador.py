"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros:
o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""

#função
def ficha(nome_jogador='<desconhecido>', num_gols=0):
    return f"O jogador {nome_jogador.upper()} fez {num_gols} gols."


#programa principal
nome = str(input('Nome do jogador: '))
gol = str(input('Número de gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    ficha(g = gol)
else:
    ficha(nome, gol)


print(ficha(nome, gol))
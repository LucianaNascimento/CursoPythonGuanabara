
"""
Faça um minissistema que utilize o interactive help do Python
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra "FIM", o programa se encerrará!.
OBS: use cores.
"""
from time import sleep

c = ('\33[m',         # 0 - sem cores
     '\33[0;30;41m',  # 1 - vermelho
     '\33[0;30;42m',  # 2 - verde
     '\33[0;30;43m',  # 3 - amarelo
     '\33[0;30;44m',  # 4 - azul
     '\33[0;30;45m',  # 5 - roxo
     '\33[7;30m',  # 6 - preto
)

def ajuda(comando):
    titulo(f'Acessando o manual do comando \'{comando}\'', 4)
    help(comando)
    sleep(2)

def titulo(texto, cor=1):
    tamanho = len(texto) + 4
    print(c[cor], end='')
    print("~" * tamanho)
    print(f"  {texto}")
    print("~" * tamanho)
    print(c[0], end='')
    sleep(1)

#programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)


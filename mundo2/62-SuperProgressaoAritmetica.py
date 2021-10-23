'''
Melhore o exercício 61, perguntando para o usuário
se ele quer mostrar mais alguns termos
O programa encerra quando ele disser que quer mostrar "0 termos"
'''

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

termo = primeiro
contador = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while contador <= total:
        print(f'{termo} - ', end='')
        termo += razao
        contador += 1
    print('Pausa')
    mais = int(input('Mais termos: '))

print('Fim.')
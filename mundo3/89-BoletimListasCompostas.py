"""
Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um
e permita que o usuário possa mostrar as notas de cada aluno individualmente
"""

ficha = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])

    resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp in 'N':
        break
print('=-' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('=-' * 30)

for indice, aluno in enumerate(ficha):
    print(f'{indice +1 :<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    print('=-' * 30)
    opc = int(input('Mostrar nota de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('Fim')















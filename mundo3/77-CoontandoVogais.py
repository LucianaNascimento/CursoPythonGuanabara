'''
Crie um programa que tenha uma tupla com várias palavras
(não usar acentos).
Depois disso, você deve mostrar, para cada palavra,
quais são as suas vogais
'''
palavras = ('aprender', 'programar','linguagem','python','curso','satudar','praticar', 'trabalhar', 'marcado',
            'programador', 'futuro')

for p in palavras:
    print(f'\n Na palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeéêiou':
            print(letra, end=' ')
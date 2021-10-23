''' Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar.
No final, mostra:
a) quantas pessoas têm mais de 18 anos
b) quantos homens foram cadastrados
c) quantas mulheres têm menos de 20 anos'''

tot18 = totHomem = totMulher = 0

while True:
    idade = int(input('Idade: \n'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M / F] \n')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == "M":
       totHomem += 1
    if sexo == "F" and idade < 20:
        totMulher
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Continuar? [S / N] \n')).strip().upper()[0]
    if resp == "N":
        break
print(f'Pessoas com mais de 18: {tot18}')
print(f'Homens cadastrados: {totHomem}')
print(f'Mulheres com menos de 20 anos: {totHomem}')


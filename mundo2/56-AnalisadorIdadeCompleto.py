''' Desenvolva um programa que leia nome, idade e sexo de 4 pessoas
No final do programa, mostre:
 - A média de idade do grupo
 - Qual é o nome do homem mais velho
 - Quantas mulheres têm menos de 20 anos
 '''

soma_idade = 0
media_idade = 0
maior_homem = 0
nome_velho = 0
total_mulher20 = 0


for p in range(1, 5):
    print(f'----- {p}ª pessoa: -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma_idade += idade

    if p == 1 and sexo in 'M':
        maior_homem = idade
        nome_velho = nome
    if sexo in 'M' and idade > maior_homem:
        maior_homem = idade
        nome_velho = nome
    if sexo in 'S' and idade > 20:
        total_mulher20 += 1

media_idade = soma_idade / 4
print(f'A média de idade do grupo é de {media_idade} anos.')
print(f'O nome do homem mais velho é {nome_velho} e ele tem {maior_homem} anos')
print(f'Ao todo são {total_mulher20} mulheres com menos de 20 anos')

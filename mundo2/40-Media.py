'''
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- média abaixo de 5.0: reprovado
- média entre 5.0 e 6,9: recuperação
- média 7.0 ou superior: aprovado
'''
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2
print(f'A média do aluno é {media}')

if 7 > media >=5:
    print('O aluno está em recuperação')
elif media < 5:
    print('O aluno está reperovado')
else:
    print('O aluno está aprovado')
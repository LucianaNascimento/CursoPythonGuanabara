# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

nome = str(input("Digite seu nome completo: \n")).strip()
print(f'Seu nome tem Silva? {"Silva" in nome}')
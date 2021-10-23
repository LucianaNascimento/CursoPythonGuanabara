# Crie um programa que leia o nome completo de uma pessoa:
#e mostre
# O nome com todas as letras maiúsculas
# O nome com todas minúsculas
# Quantas letras (sem considerar espaços)
# Quantas letras tem o primeiro nome:

nome = str(input("Digite seu nome: \n")).strip()

print(f"Nome em maiúsculas: {nome.upper()}.")
print(f"Nome em minúsculas: {nome.lower()}.")
print(f"Letras ao todo: {len(nome) - nome.count(' ')}.")
#print(f'O seu primeiro tem tem {nome.find(" ")} letras.') ou

separa = nome.split()
print(f'O primeiro nome é "{separa[0]}" e ele tem {len(separa[0])} letras.')
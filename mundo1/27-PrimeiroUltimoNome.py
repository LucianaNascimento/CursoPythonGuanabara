# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

# Ex.: Ana Maria de Souza
# Primeiro = Ana
# Último: Souza

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print(f"Seu Primeiro nome= {nome[0]}")
print(f"Seu último nome = {nome[-1]}")
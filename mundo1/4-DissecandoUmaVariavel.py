# Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele

entrada = input("Digite algo: \n")
print(f"Tipo primitivo: {type(entrada)}.")
print(f"É numérico? {(entrada.isnumeric())}")
print(f"É alfanumérico? {entrada.isalpha()}.")
print(f"É um decimal? {entrada.isdecimal()}.")
print(f"É apenas espaço em branco? {entrada.isspace()}.")
print(f"Está em maiúsculas? {entrada.isupper()}.")
print(f"Está em minúsculas? {entrada.islower()}.")
print(f'Está capitalizada? {entrada.istitle()}')
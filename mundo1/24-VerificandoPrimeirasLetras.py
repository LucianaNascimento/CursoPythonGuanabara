# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "Santo"

city = input("Digite uma cidade: \n").strip()
print(city[:5].upper() == "SANTO")
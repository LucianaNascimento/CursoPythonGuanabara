# Faça um programa que leia uma frase qualquer e mostre:
# Quantas vezes aparece a letra "a"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez


frase = str(input("Digite uma frase: \n")).upper().strip()


# Quantas vezes aparece a letra "a":
print(f"A letra A aparece {frase.count('A')} vezes na frase.")


print(f"A primeira letra A aparece na posição {frase.find('A')+1}.")


print(f"A última letra A apareceu na posição {frase.rfind('A')+1}.")
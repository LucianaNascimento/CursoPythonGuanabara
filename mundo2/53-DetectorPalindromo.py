''' Crie um programa que leia uma frase qualquer
E diga se ela é um palíndromo, desconsiderando os espaços'''
# Após a sopa
# A sacada da casa
# A torre da derrota
# o lobo ama o bolo
# Anotaram a data da maratona

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inversao = ''

for letra in range(len(junto) -1, -1, -1):
    inversao += junto[letra]
print(junto, inversao)

if inversao == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo')


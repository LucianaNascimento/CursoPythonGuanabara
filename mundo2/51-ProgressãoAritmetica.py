''' Desenvolva um programa que leia o primeiro termo e a razão
de uma PA (Progressão Aritmética).
No final, mostre os 10 primeiros termos dessa progressão.'''

primeiro = int(input('Primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
decimo = primeiro + (10 - 1) * razao  # Fórmula do enésimo termo de uma PA.
for c in range(primeiro, decimo, razao):
    print(f'{c}', end=' - ')
print("Fim.")
'''Crie um programa onde o usuario digite uma expressão qualquer que use parenteses. Seu aplicativo deverá
analisar se a expressão passada está com os parenteses abertos e fechados na oredem correta.'''

expre = str(input('Digite a expressão: '))

pilha =[]

for simb in expre:
    if simb =='(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha)> 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão é válida')
else:
    print('Sua expressão não é válida')


"""
Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto
NEGADO, OPCIONAL ou OBRIGATORIO nas eleições.
"""

#função
def voto(ano):
    from datetime import date
    atual= date.today().year
    idade = atual - ano

    if idade < 16:
        return f'Com {idade} anos de idade: NEGADO'
    elif 16<= idade < 18:
        return f"Com {idade} anos de idade: OPCIONAL"
    else:
        return f"Com {idade} anos de idade: OBRIGATÓRIO"


#programa principal
ano_nasc = int(input('Em qual ano você nasceu? '))
print(voto(ano_nasc))
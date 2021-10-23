'''
Faça um programa que leia o ano de nascimento de um jovem e informe
de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo
'''
from datetime import date

nasc = int(input("Ano de nascimento: "))
ano_atual = date.today().year
idade = (ano_atual - nasc)

if idade == 18:
    print('Você deve se alistar imediatamente')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda falatam {saldo} anos para o alistamento')
    ano = ano_atual + saldo
    print(f'Seu alistamento será em {ano}')
elif idade > 18:
    saldo = idade -18
    print(f'Você já deveria ter se alistado há {saldo} anos')
    ano = ano_atual - saldo
    print(f'Seu alistamento foi em {ano}')
'''
CDentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
 Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(),
 mas com uma validação de dados para aceitar apenas valores que seja monetários.
'''

def aumentar(preco = 0, taxa= 0, formato=False):
    res = preco + (preco * taxa /100)
    return res if formato is False else moeda(res)

def diminuir(preco= 0, taxa= 0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)

def dobro(preco= 0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)

def metade(preco= 0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)

def moeda(preco= 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')

def resumo(preco= 0, taxaAum=10, taxaRed=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaAum}% de aumento: \t{aumentar(preco, taxaAum, True)}')
    print(f'{taxaRed}% de aumento: \t{diminuir(preco, taxaRed, True)}')
    print('-' * 30)
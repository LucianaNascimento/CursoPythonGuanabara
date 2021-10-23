''' Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo
'''


while True:
    n = int(input('Qual tabuada você quer? (número negativo finaliza o programa) '))
    print('=-' * 15)
    if n < 0:
        break
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
    print('=-' * 15)
print("Programa encerrado.")
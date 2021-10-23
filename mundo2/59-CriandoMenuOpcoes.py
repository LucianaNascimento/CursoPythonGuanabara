''' Crie um programa que leia dois valores e mostre um menu
na tela:
1: somar
2: multiplicar
3: maior
4: novos números
5: sair do programa
Seu programa deverá realizar a operação solicitada em cada caso '''

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))

opcao = 0

while opcao != 5:
    print(
    '''
    [1] soma
    [2] multiplicação
    [3] maior ou menor
    [4] escolher novos números
    [5] encerrar o programa'''
    )
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = num1 + num2
        print(f'A soma entre {num1} e {num2} é igual a {soma}')

    elif opcao == 2:
        produto = num1 * num2
        print(f'O resultado de {num1}  X {num2} é igual a {produto}')

    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'Entre {num1} e {num2} o maior valor é {maior}')

    elif opcao == 4:
        print('Informe os números novamente: ')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print("Opção 5: programa encerrado.")
    else:
        print('Opção inválida, tente novamente')
    print('=-=' * 10)
print('Fim do programa, volte sempre')



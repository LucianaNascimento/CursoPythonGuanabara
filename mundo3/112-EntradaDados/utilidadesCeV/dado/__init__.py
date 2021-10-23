def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço invalido!\033[m')
        else:
            valido = True
            return float(entrada)

def leia_int(texto_usuario):
    ok = False
    value = 0
    while True:
        numero = input(f'{texto_usuario} ')
        if numero.isnumeric():
            valor = numero
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido!\033[m')
        if ok:
            break
    return valor
        #ainda falta tratamento de erro(try Catch
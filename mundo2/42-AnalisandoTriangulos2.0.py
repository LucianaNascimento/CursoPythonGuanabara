'''
Refaça o DESAFIO 35, dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado:
- equilátero: todos os lados iguais
- isósceles: dois lados iguais
- escaleno: todos os lados diferentes
'''
reta1 = float(input("Primeiro segmento de reta: "))
reta2 = float(input("Segundo segmento de reta: "))
reta3 = float(input("Terceiro segmento de reta: "))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("Os segmentos acima podem formar um triângulo ", end="")
    if reta1 == reta2 == reta3:
        print("EQUILÁTERO.")
    elif reta1 != reta2 != reta3:
        print("ESCALENO.")
    else:
        print("ISÓSCELES")
else:
    print("Os segmentos acima NÃO podem formar um triângulo")
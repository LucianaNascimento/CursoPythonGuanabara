# Faça um programa que mostre na tela
# Uma contagem regressiva para o estouro e fogos de artifício,
# Indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

for i in range(10, -1, -1):
    print(i)
    sleep(1)
print("FELIZ ANO NOVO!")
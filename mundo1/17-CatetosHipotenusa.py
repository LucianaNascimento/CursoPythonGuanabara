# Desafio 17: Faça um programa que leia o comprimento do cateto oposto (co) e do cateto adjacente (ca) de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

co = float(input("Cateto oposto: \n"))

ca = float(input("Cateto adjacente: \n"))

#hip = (co ** 2 + ca ** 2) ** (1/2)- sem a importação
hip = hypot(co, ca)


print(f"A hipotenusa dos números {co} e {ca} é {hip:.2f}.".format(co, ca, hip))
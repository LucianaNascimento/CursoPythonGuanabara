# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo

# Inclusive posso dizer qual tipo de triângulo pode ser formado.
# Não deve ser difícil isso em Python.

reta1 = float(input("Primeiro segmento de reta: \n"))
reta2 = float(input("Segundo segmento de reta: \n"))
reta3 = float(input("Terceiro segmento de reta: \n"))

if reta1 < reta2  + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("O triângulo pode ser formado.")
else:
    print("O triângulo não pode ser formado.")

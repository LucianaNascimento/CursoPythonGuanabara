# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

metro = float(input("Digite um valor em metros: \n"))

cm = metro * 100
mm = metro * 1000

print(f"{metro} metros são {cm} centímetros.")
print(f"{metro} metros são {mm} milímetros.")


#acrescimo

km = metro /1000
hectom = metro / 100
decam = metro / 10
decim = metro * 10

print(f"{metro} metros são {km} kilômetros.")
print(f"{metro} metros são {hectom} hectômetros.")
print(f"{metro} metros são {decam} decâmetros.")

print(f"{metro} metros são {decim} decímetros.")

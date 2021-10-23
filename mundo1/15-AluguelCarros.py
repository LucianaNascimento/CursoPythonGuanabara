# Aluguel de carros:

# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado

# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

dias = int(input("Por quantos dias o carro foi alugado: \n"))
km = float(input("Quantos km o carro rodou: \n"))

custo_dias = (dias * 60)
custo_km = (km * 0.15)
pagar = custo_dias + custo_km

print(f"Você andou {km}km por {dias} dias, então o preço a pagar é R$ {pagar:.2f}.")

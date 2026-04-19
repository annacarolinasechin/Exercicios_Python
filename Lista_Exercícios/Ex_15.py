# solicitar 5 valores e calcular soma total:

soma = 0

for i in range(5):
    numero = float(input(f"Digite um número: "))
    soma += numero

print(f"A soma dos 5 números resulta em: {soma}.")
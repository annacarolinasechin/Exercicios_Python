# solicitar 5 valores e exibir sua soma: 

soma = 0
for num in range(5):
    valores = float(input("Insira um valor: ").replace(",", "."))
    soma += valores

print(f"A soma dos valores resulta em: {soma}.")






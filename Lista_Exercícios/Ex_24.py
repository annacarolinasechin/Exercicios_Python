# solicitar valor e quantidade de um produto e trate possíveis erros:

while True:
    try:
        valor = float(input("Insira o valor do produto: ").replace(",", "."))
        break
    except ValueError:
        print("Insira um valor válido!")

while True:
    try:
        quant = int(input("Insira a quantidade desejada: "))
        break
    except ValueError:
        print("Insira uma quantidade válido!")

print(f"O valor: {valor}, quantidade {quant}.")
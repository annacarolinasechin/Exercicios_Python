# solicitar valor unitário, quantidade e calcular total a ser pago:

valor = float(input("Insira o valor do produto: ").replace(",", "."))
quant = int(input("Insira a quantidade desejada: "))

print(f"O valor total a ser pago é: R$ {valor*quant}.")

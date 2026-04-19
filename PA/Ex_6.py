# solicitar valor e quantidade de um produto e exibir total a ser pago: 

valor = float(input("Insira o valor do produto: ").replace(",", "."))
quant = int(input("Insira a quantidade desejada: "))

print(f"O valor total a ser pago é: {valor*quant}.")
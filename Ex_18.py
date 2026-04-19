# função que retorna valor total a ser pago (solicita valor e quantidade):

def Total(valor, quant):
    total = valor*quant
    return total

valor = float(input("Insira o valor do produto: ").replace(",", "."))
quant = int(input("Insira a quantidade do produto: "))

valor_total= Total(valor, quant)

print(f"O valor total a ser pago é: {valor_total}.")
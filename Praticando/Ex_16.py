# 16) tem uma função que receba o valor do produto e a quantidade retorne o valor a pagar

def Valor_Total(valor, quant):
    return valor * quant

def Solicitar_Valores(mensagem):
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Insira valores válidos")

valor = Solicitar_Valores("Insira o valor do produto: R$ ")
quant = Solicitar_Valores("Insira a quantidade desejada: ")

total = Valor_Total(valor, quant)

print(f"O valor total a ser pago é: R$ {total}.")
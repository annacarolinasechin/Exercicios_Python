print("SISTEMA DE VENDAS\n")
print("Dados do Usuário: \n")

while True:
    try:
        nome_cliente = input("Insira seu nome: ")
        break
    except ValueError:
        print("Insira Corretamente!")

print()
print("Informações da venda: ")
print()

while True:
    try:
        nome_produto = input("Insira o nome do produto: ")
        break
    except ValueError:
        print("Insira o nome corretamente!")


def Subtotal(valor_produto, quant_produto):
    subtotal = valor_produto*quant_produto
    return subtotal

while True:
    try:
        valor_produto = float(input("Insira o valor do produto: R$").replace(",", "."))
        break
    except ValueError:
        print("Insira valores válidos!")

while True:
    try:
        quant_produto = int(input("Insira a quantidade desejada: "))
        break
    except ValueError:
        print("Insira somente valores inteiros!")

sub_total = Subtotal(valor_produto, quant_produto)


if sub_total >= 500:
    total = sub_total - sub_total*0.10
    desconto = sub_total - total

elif sub_total >= 200 and sub_total < 500:
    total = sub_total - sub_total*0.05
    desconto = sub_total - total

else:
    total = sub_total
    desconto = sub_total - total

print()

print("RESUMO DA COMPRA")

print()

print(f"Nome do cliente: {nome_cliente};")
print(f"Subtotal: R${sub_total};")
print(f"Desconto concedido: R${desconto}")
print(f"Valor total da compra: R${total}")

input()

while True:
    nova_compra = input("Deseja realizar uma nova compra (digite 'N' caso não!)? ")
    if nova_compra == "N" or nova_compra == "n":
        print("Compra Finalizada!")
        break
    else:
        print("Insira 'N' para concluir a compra!")
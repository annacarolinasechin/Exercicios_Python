# determinar se compra terá desconto:

valor = float(input("Insira o valor da compra: R$ ").replace(",", "."))

if valor >= 100:
    print("Você terá desconto!")

else:
    input("Você não terá desconto!")
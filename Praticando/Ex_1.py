# informar se o cliente teve desconto (compra acima de R$100):

while True:
    try:
        valor = float(input("Insira o valor da compra: R$ ").replace(",", ","))
        if valor >= 100:
            print("Você terá desconto!")
        else:
            print("Você não terá desconto!")
        break
    except ValueError:
        print("Insira valores válidos!")
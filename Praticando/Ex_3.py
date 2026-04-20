# crie um programa para o pagamento de comissão de vendedores levando em consideração que sua comissão é de 5% do valor total:

while True:
    try:
        valor = float(input("Insira o valor total da compra: R$ ").replace(",", "."))
        break
    except ValueError:
        print("Insira valores válidos!")

print(f"O valor da comissão desta compra resulta em: {valor*0.05}.")
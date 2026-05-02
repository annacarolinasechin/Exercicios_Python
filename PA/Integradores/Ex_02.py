print("\n----------- CADASTRO PRODUTOS ------------")

Lista_Produtos = []

quantidade = int(input("\nDeseja cadastrar quantos produtos? "))

for i in range(quantidade):

    nome = input("\nInsira o NOME do produto: ")
    valor = float(input("Insira o VALOR do produto: R$").replace(",", "."))
    estoque = int(input("Insira a QUANTIDADE em estoque: "))

    Dados_Produto = {
        "nome": nome,
        "valor": valor,
        "estoque": estoque
    }


    Lista_Produtos.append(Dados_Produto)
    
print("\n----------- DADOS PARA COMPRA ------------")

nome_cliente = input("\nInsira seu nome: ")

while True:

    quant_compras = int(input("\nDeseja comprar QUANTOS produtos? "))

    total = 0

    for i in range(quant_compras):
        nome_produto = input("Insira o NOME do produto desejado: ")
        j = 0
        produtoEncontrado = False
        while j < len(Lista_Produtos):
            if nome_produto.lower() == Lista_Produtos[j]["nome"].lower():
                produtoEncontrado = True
                print("Produto encontrado!\n")

                quant_desejada = int(input("Insira a QUANTIDADE desejada: "))
                subtotal = Lista_Produtos[j]["valor"] * quant_desejada
                total += subtotal
                break
            j = j + 1

        if produtoEncontrado == False:
            print("Produto não encontrado.")
            break

    if total >= 1000:
        total_final = total - total*0.15
        desconto = total - total_final

    elif total >= 500:
        total_final = total - total*0.10
        desconto = total - total_final

    elif total >= 200:
        total_final = total - total*0.05
        desconto = total - total_final

    else:
        total_final = total
        desconto = total - total_final

    print("\n----------- RESUMO DA VENDA ------------\n")

    print(f"Cliente: {nome_cliente};")
    print(f"Subtotal: R${total:.2f};")
    print(f"Desconto: R${desconto:.2f};")
    print(f"Total: R${total_final:.2f}.\n")

    print("\n----------- AGRADECEMOS PELA PREFERÊNCIA! ------------\n")

    novas_compras = input("Deseja realizar novas compras (S/N)? ")

    if novas_compras.upper() == "N":
        print("\nCompra finalizada!\n")
        break
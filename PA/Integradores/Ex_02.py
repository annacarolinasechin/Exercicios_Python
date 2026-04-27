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

<<<<<<< HEAD
nome_cliente = input("\nInsira seu nome: ")

while True:

    quant_compras = int(input("\nDeseja comprar QUANTOS produtos? "))

=======
nome_cliente = input("Insira seu nome: ")
while True:
    quant_compras = int(input("Deseja comprar QUANTOS produtos? "))
    
>>>>>>> 78ddbb4c78253ef6661efc6a9d37e97e21592464
    total = 0
    for i in range(quant_compras):
        nome_produto = input("Insira o NOME do produto desejado: ")
        j = 0
        produtoEncontrado = False
        while j < len(Lista_Produtos):
<<<<<<< HEAD
            if nome_produto.lower() == Lista_Produtos[j]["nome"].lower():
                produtoEncontrado = True
                print("Produto encontrado!\n")
=======
            if nome_produto == Lista_Produtos[j]["nome"]:
                produtoEncontrado = True
                print("Produto encontrado!")
>>>>>>> 78ddbb4c78253ef6661efc6a9d37e97e21592464
                quant_desejada = int(input("Insira a QUANTIDADE desejada: "))
                subtotal = Lista_Produtos[j]["valor"] * quant_desejada
                total += subtotal
                break
            j = j + 1
<<<<<<< HEAD

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
=======
    
        if produtoEncontrado == False:
            print("Produto não encontrado.")
            break
    novas_compras = input("Deseja realizar novas compras (S/N)? ")
    if novas_compras == "N" or novas_compras == "n":
            print("Compra finalizada!\n")
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

>>>>>>> 78ddbb4c78253ef6661efc6a9d37e97e21592464

    novas_compras = input("Deseja realizar novas compras (S/N)? ")

<<<<<<< HEAD
    if novas_compras.upper() == "N":
        print("\nCompra finalizada!\n")
        break
=======
    print("AGRADECEMOS PELA COMPRA!")
>>>>>>> 78ddbb4c78253ef6661efc6a9d37e97e21592464

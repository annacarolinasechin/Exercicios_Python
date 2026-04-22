print("SISTEMA DE CADASTRO\n")
print("CADASTRANDO PRODUTOS\n")

Lista_Produtos = []

quantidade = int(input("Deseja cadastrar quantos produtos? \n"))

for i in range(quantidade):

    nome = input("Insira o NOME do produto: ")
    valor = float(input("Insira o VALOR do produto: R$").replace(",", "."))
    estoque = int(input("Insira a QUANTIDADE em estoque: "))

    Dados_Produto = {
        "nome": nome,
        "valor": valor,
        "estoque": estoque
    }


    Lista_Produtos.append(Dados_Produto)
    
print("DADOS PARA COMPRA\n")

nome_cliente = input("Insira seu nome: ")

quant_compras = int(input("Deseja comprar QUANTOS produtos? "))

total = 0
for i in range(quant_compras):
    nome_produto = input("Insira o NOME do produto desejado: ")
    j = 0
    produtoEncontrado = False
    while j < len(Lista_Produtos):
        if nome_produto == Lista_Produtos[j]["nome"]:
            produtoEncontrado = True
            print("Produto encontrado!")
            quant_desejada = int(input("Insira a QUANTIDADE desejada: "))
            subtotal = Lista_Produtos[j]["valor"] * quant_desejada
            total += subtotal
            break
        j = j + 1

    if produtoEncontrado == False:
        print("Produto não encontrado.")
        break

while True:

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

    while True:
        novas_compras = input("Deseja realizar novas compras (S/N)? ")

        if novas_compras == "N" or novas_compras == "n":
            print("Compra finalizada!\n")
            break


    print("RESUMO DA VENDA:")
    print(f"Nome: {nome_cliente};")
    print(f"Subtotal: {total};")
    print(f"Desconto: {desconto};")
    print(f"Total: {total_final};\n")

    print("AGRADECEMOS PELA COMPRA!")
def desconto_aplicado(total):
    if total >= 1000:
        percentual = 0.15
    elif total >= 500:
        percentual = 0.10
    elif total >= 200:
        percentual = 0.05
    else:
        return 0
    desconto = total * percentual
    return desconto

def subtotal_compra(prod, prod_quant):
    return prod["valor"] * prod_quant

def total_compras(clientes):
    total = 0
    for cliente in clientes:
        total += cliente["total"]
    return total

def media_compras(clientes):
    if len(clientes) == 0:
        return 0
    return total_compras(clientes) / len(clientes)

def maior_compra(clientes):
    if len(clientes) == 0:
        return None
    maior = clientes[0]
    for cliente in clientes:
        if cliente["total"] > maior["total"]:
            maior = cliente
    return maior

prod_cadastrados = []
clientes = []
novas_compras = True
adicionar = True
comprando = True

while novas_compras:
    total = 0

    while adicionar:
        print("\n----------- CADASTRO PRODUTO ------------\n")

        while True:
            try:
                prod_nome = input("Insira o NOME do produto: ")
                break
            except ValueError:
                print("Insira corretamente!")

        while True:
            try:
                prod_valor = float(input("Insira o VALOR do produto: R$").replace(",", "."))
                break
            except ValueError:
                print("Entrada inválida, tente novamente!")

        while True:
            try:
                prod_estoque = int(input("Insira a QUANTIDADE em estoque: "))
                break
            except ValueError:
                print("Insira somente números inteiros!")

        novo_cadastro = input("\nDeseja CADASTRAR um novo produto? (S/N) ")

        if novo_cadastro.upper() == "S":
            adicionar = True

        else:
            adicionar = False
            print("\nConcluído!\n")
                
        cadastro_produtos = {
            "nome": prod_nome,
            "valor": prod_valor,
            "estoque": prod_estoque
        }

        prod_cadastrados.append(cadastro_produtos)


    print("\n----------- DADOS PARA COMPRA ------------")
    cli_nome = input("\nInsira SEU nome: ")

    print("\n----------- PRODUTOS DISPONÍVEIS ------------\n")
    for produto in prod_cadastrados:
        print(f"\nNome: {produto['nome']} | Preço: {produto['valor']} | Estoque: {produto['estoque']}")

    while comprando:
        while True:
            prod_desejado = input("\nInsira o NOME do produto desejado: ")
            prod_encontrado = False

            for prod in prod_cadastrados:
                if prod["nome"].upper() == prod_desejado.upper():
                    prod_encontrado = True

                    print("\n*Produto encontrado!*\n")

                    while True:
                        try:
                            prod_quant = int(input("Insira a QUANTIDADE desejada: "))
                            break
                        except ValueError:
                            print("Insira corretamente!")

                    if prod_quant > prod["estoque"]:
                        print(f"Estoque insuficiente! Disponível: {prod['estoque']}")
                        continue
                    break
            
            if not prod_encontrado:
                print("Produto não encontrado, tente novamente!")
            else:
                break

        mais_produtos = input("\nDeseja adicionar outro produto? (S/N): ")
        comprando = mais_produtos.upper() == "S"

        subtotal = subtotal_compra(prod, prod_quant)
        total += subtotal

    desconto = desconto_aplicado(total)

    clientes.append({"nome": cli_nome, "total": total - desconto})

    print("\n----------- RESUMO DA VENDA ------------\n")
    print(f"Cliente: {cli_nome}")
    print(f"Subtotal: R${subtotal:.2f}")
    print(f"Desconto: R${desconto:.2f}")
    print(f"Total final: R${total - desconto:.2f}")


    novas_compras = input("\nDeseja realizar outra venda? (S/N): ")
    if novas_compras.upper() == "S":
            novas_compras = True
            adicionar = True
        
    else:
        novas_compras = False
        adicionar = False
        print("\n----------- RELATÓRIO GERAL ------------\n")
        for cliente in clientes:
            print(f"Cliente: {cliente['nome']} | Valor gasto: R${cliente['total']}")
            
        print(f"\nTotal arrecadado: R${total_compras(clientes):.2f}")
        print(f"Média das compras: R${media_compras(clientes):.2f}")

        maior = maior_compra(clientes)
        print(f"Maior compra: {maior['nome']} | R${maior['total']:.2f}")
        print("\n------- AGRADECEMOS A PREFERÊNCIA -------\n")
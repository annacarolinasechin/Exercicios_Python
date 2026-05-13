def calcular_subtotal(valor, quantidade):
    return valor * quantidade

def aplicar_desconto(total):
    if total >= 1000:
        percentual = 0.15
    elif total >= 500:
        percentual = 0.10
    elif total >= 200:
        percentual = 0.05
    else:
        return 0
    return total * percentual


def calcular_media(total_vendas):
    if not total_vendas:
        return 0
    total_geral = 0
    for venda in total_vendas:
        total_geral += venda["total"]
    return total_geral / len(total_vendas)


def encontrar_maior_compra(total_vendas):
    if not total_vendas:
        return None
    maior = total_vendas[0]
    for venda in total_vendas:
        if venda["total"] > maior["total"]:
            maior = venda
    return maior


prod_cadastrados = []
total_vendas = []
continuar = True
reiniciar = True

while reiniciar:

    while continuar:
        print("\n----------- CADASTRO PRODUTO ------------\n")

        while True:
            try:
                prod_nome = input("\nInsira o NOME do produto: ")
                break
            except ValueError:
                print("Insira corretamente!")

        while True:
            try:
                prod_valor = float(input("Insira o VALOR do produto: R$").replace(",", "."))
                if prod_valor > 0:
                    break
                else:
                    print("Entrada inválida, tente novamente!")
            except ValueError:
                print("Entrada inválida, tente novamente!")

        while True:
            try:
                prod_estoque = int(input("Insira a QUANTIDADE em estoque: "))
                if prod_estoque > 0:
                    break
                else:
                    print("Insira somente números inteiros!")
            except ValueError:
                print("Insira somente números inteiros!")

        prod_cadastrados.append({
            "nome": prod_nome,
            "valor": prod_valor,
            "estoque": prod_estoque
        })

        while True:
            try:
                novo_cadastro = input("\nDeseja CADASTRAR novo produto? (S/N) ")
                if novo_cadastro.upper() == "S":
                    continuar = True
                    break
                elif novo_cadastro.upper() == "N":
                    continuar = False
                    break
                else:
                    print("\nS ou N!")
            except ValueError:
                print("APENAS S / N!!!!!!!!!")


    continuar_vendas = True

    while continuar_vendas:

        print("\n----------- DADOS PARA COMPRA ------------")
        cli_nome = input("\nInsira SEU nome: ")

        total = 0
        add_produtos = True

        while add_produtos:

            print("\n----------- PRODUTOS DISPONÍVEIS ------------\n")
            for nomes in prod_cadastrados:
                print(f"Nome: {nomes['nome']} | Preço: R${nomes['valor']:.2f} | Estoque: {nomes['estoque']}\n")

            while True:
                prod_desejado = input("\nInsira o NOME do produto desejado: ")
                prod_encontrado = False

                for prod in prod_cadastrados:
                    if prod["nome"].upper() == prod_desejado.upper():
                        prod_encontrado = True
                        print("**Produto encontrado!**")

                        while True:
                            try:
                                prod_quant = int(input("Insira a QUANTIDADE desejada: "))
                                if prod_quant <= 0:
                                    print("Insira quantidade válida!")
                                    continue
                                if prod_quant > prod["estoque"]:
                                    print("Estoque insuficiente!")
                                    continue
                                break
                            except ValueError:
                                print("Digite apenas números!")

                        subtotal = calcular_subtotal(prod["valor"], prod_quant)
                        total += subtotal
                        prod["estoque"] -= prod_quant
                        break

                if not prod_encontrado:
                    print("Produto não encontrado, tente novamente!")
                else:
                    break

            while True:
                novo_produto = input("\nDeseja ADICIONAR novo produto (S/N)? ")
                if novo_produto.upper() == "S":
                    add_produtos = True
                    break
                elif novo_produto.upper() == "N":
                    add_produtos = False
                    break
                else:
                    print("\nInsira apenas S ou N!")

        desconto = aplicar_desconto(total)
        total_final = total - desconto

        print("\n----------- RESUMO DA VENDA ------------\n")
        print(f"Subtotal: R${total:.2f}")
        print(f"Desconto: R${desconto:.2f}")
        print(f"Total final: R${total_final:.2f}")

        total_vendas.append({
            "cliente": cli_nome,
            "total": total_final
        })

        while True:
            try:
                nova_venda = input("\nDeseja realizar nova venda? (S/N): ")
                if nova_venda.upper() == "S":
                    continuar_vendas = True
                    break
                elif nova_venda.upper() == "N":
                    continuar_vendas = False
                    break
                else:
                    print("Entrada inválida!")
            except ValueError:
                print("Inválido")

    total_geral = 0
    for venda in total_vendas:
        total_geral += venda["total"]

    maior_compra = encontrar_maior_compra(total_vendas)
    media = calcular_media(total_vendas)

    print("\n----------- RELATÓRIO ------------\n")
    for venda in total_vendas:
        print(f"Cliente: {venda['cliente']} | Total gasto: R${venda['total']:.2f}")

    print(f"\nTotal de vendas: {len(total_vendas)}")
    print(f"Total somado: R${total_geral:.2f}")
    print(f"Cliente com MAIS compras realizadas: {maior_compra['cliente']} (R${maior_compra['total']:.2f})")
    print(f"Média das vendas: R${media:.2f}")

    while True:
        try:
            reinicio = input("\nDeseja REINICIAR todas as vendas/produtos cadastrados (S/N)? ")
            if reinicio.upper() == "S":
                reinicio = True
                continuar = True
                continuar_vendas = True
                prod_cadastrados = [] 
                total_vendas = []
                break
            elif reinicio.upper() == "N":
                reinicio = False
                print("\nConcluído!")
                break
            else:
                print("\nS ou N!")
        except ValueError:
            print("\nS ou N!")
def desconto_aplicado(total): # função que aplica desconto sob valor total da compra (valor de cada produto * quantidade desejada)
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

def subtotal_compra(prod, prod_quant): # função que calcula subtotal da compra;
    return prod["valor"] * prod_quant # tem como retorno o valor de cada produto * quantidade desejada

def total_compras(clientes): # função que calcula total de todas as compras realizadas (considerando diferentes clientes)
    total = 0
    for cliente in clientes:
        total += cliente["total"]
    return total

def media_compras(clientes): # função que calcula média total de todas as compras realizadas (considerando diferentes clientes)
    if len(clientes) == 0:
        return 0
    return total_compras(clientes) / len(clientes)

def maior_compra(clientes): # função que determina qual maior compra realizada (considerando diferentes clientes)
    if len(clientes) == 0:
        return None
    maior = clientes[0]
    for cliente in clientes:
        if cliente["total"] > maior["total"]:
            maior = cliente
    return maior

prod_cadastrados = [] # lista para armazenar cada dicionário criado (produto cadastrado)
clientes = [] # lista que armazena as informações que desejamos de cada cliente (nome e valor gasto)
novas_compras = True # condição que vai nortear todo o programa e permitir que ele se repeta por completo (se for verdadeira)
adicionar = True # condição que, quando verdadeira, permite que o usuário cadastre novos produtos
comprando = True # condição que, quando verdadeira, permite ao usuário adicionar novos produtos a sua compra

while novas_compras: # laço que vai funcionar ENQUANTO "novas_compras" (que serve como norteador) for verdadeira e se for o caso, eventualmente, vai permitir que todo o programa se repita
    total = 0 # variável que mais tarde, vai receber valor total da compra (é preciso declara-la previamente)

    while adicionar: # laço que vai funcionar ENQUANTO "adicionar" (que vai permitir que o usuário cadastre novos produtos) for verdadeira
        print("\n----------- CADASTRO PRODUTO ------------\n") # printa na tela o texto (serve para "guiar" melhor o usuário quanto a cada etapa)

        while True:
            try:
                prod_nome = input("Insira o NOME do produto: ") # solicita ao usuário o nome do produto que pretende cadastrar já o armazenando
                break
            except ValueError:
                print("Insira corretamente!")

        while True:
            try:
                prod_valor = float(input("Insira o VALOR do produto: R$").replace(",", ".")) # solicita ao usuário o valor do produto que pretende cadastrar já o armazenando (.replace(",", ".") converter vírgulas inseridas em pontos. como python já reserva seu uso a separação de parâmetros, os pontos são utilizados para qualquer valor decimal ser "lido" corretamente)
                break
            except ValueError:
                print("Entrada inválida, tente novamente!")

        while True:
            try:
                prod_estoque = int(input("Insira a QUANTIDADE em estoque: ")) # solicita ao usuário a quantidade do produto que pretende cadastrar já o armazenando
                break
            except ValueError:
                print("Insira somente números inteiros!")

        novo_cadastro = input("\nDeseja CADASTRAR um novo produto? (S/N) ") # pergunta se usuário deseja cadastrar um novo produto e adiciona a variável sua resposta

        if novo_cadastro.upper() == "S": # condicional que compara devolutiva do usuário com o "esperado" (.upper() converte texto inserido para letra maiúscula, garantindo que "S" seja possível, simplificando o processo)
            adicionar = True # caso a devolutiva do usuário for a esperada, a variável "adicionar" se mantém como verdadeira (portanto, o laço responsável pelo cadastro de novos produtos vai se repetir)

        else: # condional que trata de qualquer devolutiva "para além do esperado"
            adicionar = False #caso a devolutiva do usuário for a esperada, a variável "adicionar" se tornara falsa (portanto, o laço responsável pelo cadastro de novos produtos será interrompido)
            print("\nConcluído!\n") # printa na tela que o processo de cadastro de produtos chegou ao fim (forma de nortear usuário)
                
        cadastro_produtos = { # dicionário que, a cada produto criado, registra suas respectivas informações
            "nome": prod_nome, # chave "nome" recebe valor atribuido pelo usuário em "prod_nome"
            "valor": prod_valor, # chave "valor" recebe valor atribuido pelo usuário em "prod_valor"
            "estoque": prod_estoque # chave "estoque" recebe valor atribuido pelo usuário em "prod_estoque"
        }

        prod_cadastrados.append(cadastro_produtos) # cada um dos dicionários criados vai ser adicionado ao final da lista "prod_cadastrados" (.append() adiciona dicionários criados ao fim da lista)


    print("\n----------- DADOS PARA COMPRA ------------") # printa na tela que "agora", é momento de inserir dados para compra (serve como "separador", nortear usuário)
    cli_nome = input("\nInsira SEU nome: ") # solicita ao usuário seu nome, já o armazenando

    print("\n----------- PRODUTOS DISPONÍVEIS ------------\n") # printa na tela que "agora", é momento de "visualizar" os produtos (e sua informações) que podem ser comprados (serve como "separador", nortear usuário)
    for produto in prod_cadastrados: # laço percorre lista e todos os valores adquiridos são movidos para a variável "produto" (que possibilita a manipulação das informações presentes na lista agora que não estão de fato)
        print(f"\nNome: {produto['nome']} | Preço: {produto['valor']} | Estoque: {produto['estoque']}") # é printado na tela as informações de cada produto (nome, valor e estoque, respectivamente)

    while comprando: # laço que vai funcionar ENQUANTO "comprando" (que vai permitir que o usuário realize a compra de fato) for verdadeira
        
        while True: # laço que ENQUANTO for verdadeiro, vai permitir que o usuário insira nome/quantidade do produto desejado e em seguida, verificar se os mesmos são presentes/possíveis de adquirir
            prod_desejado = input("\nInsira o NOME do produto desejado: ") # solicita ao usuário o nome do produto desejado, já o armazenando
            prod_encontrado = False # atráves dessa variável, é inicialmente resumido que produto nenhum foi encontrado

            # laço que percorre lista de produtos cadastrados e em seguida, permite saber se dados inseridos pelo usuário são presentes
            for prod in prod_cadastrados: # percorre lista e todos os valores adquiridos são movidos para a variável "prod" (que possibilita a manipulação das informações presentes na lista agora que não estão de fato)
                if prod["nome"].upper() == prod_desejado.upper(): # condicional que compara valor presente na chave "valor" em qualquer dicionário presente na lista com o nome inserido pelo usuário com (.upper() converte texto inserido para letra maiúscula, garantindo que "S" seja possível, simplificando o processo)
                    prod_encontrado = True # caso valor for correspondente a algum presente, "prod_encontrado "deixa de ser falsa

                    print("\n*Produto encontrado!*\n") # printa na tela que produto foi encontrado (norteia usuário)

                    while True:
                        try:
                            prod_quant = int(input("Insira a QUANTIDADE desejada: ")) # solicita ao usuário a quantidade desejada do produto, já a armazenando
                            break
                        except ValueError:
                            print("Insira corretamente!")

                    if prod_quant > prod["estoque"]: # condicional que compara a quantidade desejada pelo usuário com todos os presentes na lista 
                        print(f"Estoque insuficiente! Disponível: {prod['estoque']}") # se a quantidade desejada for maior que a esperada, isso é exibido
                        continue # programa continua 
                    break # laço é interrompido
            
            if not prod_encontrado: # se produto não for encontrado
                print("Produto não encontrado, tente novamente!") # printa na tela que produto não foi encontrado (norteia usuário)
            else:
                break # laço é interrompido

        mais_produtos = input("\nDeseja adicionar outro produto? (S/N): ")  # pergunta se usuário deseja adicionar um novo produto e adiciona a variável sua resposta
        comprando = mais_produtos.upper() == "S" # aqui, a resposta do usuário seja "S"/"s", a variável "comprando" vai se repetir (consequentemente, usuário vai poder adicionar novos produtos a sua compra)

        subtotal = subtotal_compra(prod, prod_quant) # a função "subtotal_compra" é chamada e recebe como parâmetros "prod" (variável que recebeu os valores extraidos da lista) e "prod_quant" (inserida pelo usuário) e seu resultado será adicionado a variável em questão
        total += subtotal  # o valor presente em "subtotal" será somado/acumulado em "total" (declarada anteriormente)

    desconto = desconto_aplicado(total) # a função "desconto_aplicado" é chamada é recebe como parâmetro "total"/seu valor e seu resultado será adicionado a variável em questão

    clientes.append({"nome": cli_nome, "total": total - desconto}) # será adicionado ao final da lista "clientes" o "nome" e "total" gasto por cada cliente (isso em formato de dicionário)

    print("\n----------- RESUMO DA VENDA ------------\n") # printa que "agora", o resumo da venda está sendo exibido (para nortear melhor usuário)
    print(f"Cliente: {cli_nome}") # é printado o nome do cliente
    print(f"Subtotal: R${subtotal:.2f}") # é printado o subtotal da compra (:.2f serve para limitar até qual casa decimal o valor será exibido, nesse caso, até a segunda)
    print(f"Desconto: R${desconto:.2f}") # é printado o desconto aplicado a compra (:.2f serve para limitar até qual casa decimal o valor será exibido, nesse caso, até a segunda)
    print(f"Total final: R${total - desconto:.2f}") # é printado o total da compra (:.2f serve para limitar até qual casa decimal o valor será exibido, nesse caso, até a segunda)


    novas_compras = input("\nDeseja realizar outra venda? (S/N): ") # pergunta se usuário deseja realizar novo produto e adiciona a variável sua resposta (assim, todo o processo será reiniciado)
    if novas_compras.upper() == "S": # condicional que compara devolutiva do usuário com o "esperado" (.upper() converte texto inserido para letra maiúscula, garantindo que "S" seja possível, simplificando o processo)
            novas_compras = True # se a resposta for correspondente, "novas_compras" volta a ser verdadeira e consequentemente, será repetida
            adicionar = True # se a resposta for correspondente, "adicionar" volta a ser verdadeira e consequentemente, será repetida
        
    else: # se a resposta for diferente
        novas_compras = False # "novas_compras" permanece falsa e consequentemente, não será repetida
        adicionar = False # "adicionar" permanece falsa e consequentemente, não será repetida
        print("\n----------- RELATÓRIO GERAL ------------\n") # printa na tela que "agora", o relatório de tudo será exibido
        for cliente in clientes: # percorre lista e todos os valores adquiridos são movidos para a variável "clientes" (que possibilita a manipulação das informações presentes na lista agora que não estão de fato)
            print(f"Cliente: {cliente['nome']} | Valor gasto: R${cliente['total']}") # printa nome e valor gasto por cada cliente, respectivamente
            
        print(f"\nTotal arrecadado: R${total_compras(clientes):.2f}") # printa valor total arrecada de todas as compras somadas ("total_compras(clientes)" é chamada diretamente e recebe como parâmetro a lista "clientes")
        print(f"Média das compras: R${media_compras(clientes):.2f}")  # printa média de todas as compras somadas ("total_compras(clientes)" é chamada diretamente e recebe como parâmetro a lista "clientes")

        maior = maior_compra(clientes) # função "maior_compra" é chamada e recebe como parâmetro a lista clientes e já tem seu resultado armazenado
        print(f"Maior compra: {maior['nome']} | R${maior['total']:.2f}") # é printado na tela nome do cliente com compra de maior valor ("maior" recebe os valores presentes nas chaves "nome" e "total")
        print("\n------- AGRADECEMOS A PREFERÊNCIA -------\n") # printa agradecimento ao usuário
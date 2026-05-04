alunos = [] # lista para armazenar cada dicionário criado (aluno cadastrado)
continuar = True

print("\n----------- CADASTRO ALUNOS -----------")

while continuar:  # laço que vai funcionar ENQUANTO "continuar" (que vai permitir que o novos alunos sejam cadastrados) for verdadeira

    while True:
        try:
            nome_aluno = input("\nNome do aluno: ") # solicita ao usuário o nome do aluno que pretende cadastrar já o armazenando
            break
        except ValueError:
            print("Insira corretamente!")

    while True:
        try:
            idade_aluno = int(input("Idade do aluno: ")) # solicita ao usuário a idade do aluno que já a armazenando
            if idade_aluno > 0: # condicional que confere se a idade do aluno em questão não é um valor negativo
                break # caso o critério tenha sido atingido (nota maior que 0), o laço é interrompido
            else:
                print("Insira uma idade válida (acima de 0!)") # é exibido caso o usuário insira algum valor número fora do esperado (portanto, negativo)
        except ValueError:
            print("Insira uma idade válida (acima de 0!)") # é exibido caso o usuário insira qualquer carácter fora do esperado no geral (letras, carácteres especiais, etc)
    
    while True:
        try:
            nota_aluno = float(input("Nota do aluno (0 a 10): ").replace(",", "."))  # solicita ao usuário a idade do aluno que já a armazenando (.replace(",", ".") converter vírgulas inseridas em pontos. como python já reserva seu uso a separação de parâmetros, os pontos são utilizados para qualquer valor decimal ser "lido" corretamente)
            if nota_aluno >= 0 and nota_aluno <= 10: # condicional que confere se a nota inserida é maior que zero e menor que 10
                break # caso o critério tenha sido atingido (a nota inserida é maior que zero e menor que 10), o laço é interrompido
            else:
                print("Insira notas entre 0 e 10!") # é exibido caso o usuário insira algum valor número fora do esperado (portanto, valores negativos ou acima do estipulado)
        except ValueError:
            print("Insira notas entre 0 e 10!") # é exibido caso o usuário insira qualquer carácter fora do esperado no geral (letras, carácteres especiais, etc)

    novo_cadastro = input("Deseja realizar um novo cadastro (S/N)? ") # pergunta se usuário deseja cadastrar um novo produto e adiciona a variável sua resposta

    if novo_cadastro.upper() == "S":  # condicional que compara devolutiva do usuário com o "esperado" (.upper() converte texto inserido para letra maiúscula, garantindo que "S" seja possível, simplificando o processo)
        continuar = True # caso a devolutiva do usuário corresponda com a esperada, a variável "continuar" se mantém como verdadeira (portanto, o laço responsável pelo cadastro de novos alunos vai se repetir)

    else: # condional que trata de qualquer devolutiva "para além do esperado"
        continuar = False # caso a devolutiva do usuário for diferente da esperada, a variável "adicionar" se tornara falsa (portanto, o laço responsável pelo cadastro de novos produtos será interrompido)
        print("Concluído! \n")

    
    cadastro_aluno = { # dicionário que, a cada produto criado, registra suas respectivas informações
        "nome": nome_aluno, # chave "nome" recebe valor atribuido pelo usuário em "nome_aluno"
        "idade": idade_aluno, # chave "idade" recebe valor atribuido pelo usuário em "idade_aluno"
        "nota": nota_aluno # chave "nota" recebe valor atribuido pelo usuário em "nota_aluno"
    }

    alunos.append(cadastro_aluno) # cada um dos dicionários criados vai ser adicionado ao final da lista "alunos" (.append() adiciona dicionários criados ao fim da lista)


def Situação_Aluno(nota_aluno): # função que determina "situação" do aluno (aprovação, recuperação e reprovação) atráves da nota inserida
    if nota_aluno >= 7:
        return "Aprovado!"
    elif nota_aluno >= 5 and nota_aluno < 7:
        return "Recuparação!"
    else:
        return "Reprovado"

situacao = Situação_Aluno(nota_aluno) # função "situação_aluno" é chamada e recebe como parâmetro a nota do aluno e seu resultado será armazenado na variável em questão

def Media_Turma(alunos): # função que calcula média de todas as notas de todos os alunos
    soma = 0
    for notas in (alunos): # lista alunos é percorrida e os valores recolhidos da chave desejada (["nota"]) são movidos para "notas"
        soma += notas["nota"] # variável soma passa a somar todos os valores recolhidos da chave "nota"
    
    try:
        return soma/len(alunos) # o retorno da função (valor que podemos manipular em qualquer outro lugar do código) consiste na divisão de todas as notas somas pela quantidad de alunos na lista
    except ZeroDivisionError:
        pass # permite que o código não quebre caso a divisão resulte em zero
    
media = Media_Turma(alunos) # função "media_turma" é chamada e recebe como parâmetro a lista de alunos e seu resultado será armazenado na variável em questão

print("----------------- RESULTADO -----------------\n")


for aluno in alunos: # laço percorre lista "alunos" e as informações desejadas são movidas para a "aluno"
    print(f"Nome: {aluno['nome']} | Idade: {aluno['idade']} | Nota: {aluno['nota']} | Situação: {Situação_Aluno(aluno['nota'])}\n")
    # é printado na tela, respectivamente: o nome, idade, nota e a situação do aluno (aqui a função é chamada diretamente é já recebe seu parâmetro) atráves de "aluno" e do valor presente na chave desejada

print(f"Média da turma: {media:.2f}\n") # é printado na tela a média da turma (calculada anteriormente)

aprovados = 0
rec = 0
reprovados = 0

for aluno in alunos: # laço percorre mais uma vez a lista, agora com o intuíto de recolher os valores presentes na chave "nota" e realizar comparações com as notas necessárias para determinar quandos alunos foram, respectivamente
        if aluno["nota"] >= 7:
            aprovados += 1 # aprovados
        elif aluno["nota"] >= 5 and aluno["nota"] < 7:
            rec += 1 # ficaram de recuperação
        else:
            reprovados += 1 # reprovaram

print(f"Aprovados: {aprovados}")
print(f"Recuperação: {rec}")
print(f"Reprovados: {reprovados}\n")
# é printado na tela, respectivamente, a quantidade de alunos que foram: aprovados, ficaram de recuperação e foram reprovados

maior_nota = alunos[0]
menor_nota = alunos[0]

for aluno in alunos: # lista é percorrida novamente, mas agora com o intuíto de recolher os valores presentes na chaves "nota" e adiciona-los a "aluno"
    if aluno["nota"] > maior_nota["nota"]:
        maior_nota = aluno

    if aluno["nota"] < menor_nota["nota"]:
        menor_nota = aluno

print(f"Aluno com maior nota: {maior_nota['nome']} - ({maior_nota['nota']})")
print(f"Aluno com menor nota: {menor_nota['nome']} - ({menor_nota['nota']})")
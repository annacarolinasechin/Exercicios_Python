alunos = []
continuar = True

print("\n----------- CADASTRO ALUNOS -----------")

while continuar:

    while True:
        try:
            nome_aluno = input("\nNome do aluno: ")
            break
        except ValueError:
            print("Insira corretamente!")

    while True:
        try:
            idade_aluno = int(input("Idade do aluno: "))
            if idade_aluno > 0:
                break
            else:
                print("Insira uma idade válida (acima de 0!)")
        except ValueError:
            print("Insira uma idade válida (acima de 0!)")
    
    while True:
        try:
            nota_aluno = float(input("Nota do aluno (0 a 10): ").replace(",", "."))
            if nota_aluno >= 0 and nota_aluno <= 10:
                break
            else:
                print("Insira notas entre 0 e 10!")
        except ValueError:
            print("Insira notas entre 0 e 10!")

    novo_cadastro = input("Deseja realizar um novo cadastro? (S/N) ")

    if novo_cadastro.upper() == "S":
        continuar = True

    else:
        continuar = False
        print("Concluído! \n")

    
    cadastro_aluno = {
        "nome": nome_aluno,
        "idade": idade_aluno,
        "nota": nota_aluno
    }

    alunos.append(cadastro_aluno)


def Situação_Aluno(nota_aluno):
    if nota_aluno >= 7:
        return "Aprovado!"
    elif nota_aluno >= 5 and nota_aluno < 7:
        return "Recuparação!"
    else:
        return "Reprovado"

situacao = Situação_Aluno(nota_aluno)

def Media_Turma(alunos):
    soma = 0
    for notas in (alunos):
        soma += notas["nota"]
    
    try:
        return soma/len(alunos)
    except ZeroDivisionError:
        pass
    
media = Media_Turma(alunos)

print("----------------- RESULTADO -----------------\n")


for aluno in alunos:
    print(f"Nome: {aluno['nome']} | Idade: {aluno['idade']} | Nota: {aluno['nota']} | Situação: {Situação_Aluno(aluno['nota'])}\n")

print(f"Média da turma: {media:.2f}\n")

aprovados = 0
rec = 0
reprovados = 0

for aluno in alunos:
        if aluno["nota"] >= 7:
            aprovados += 1
        elif aluno["nota"] >= 5 and aluno["nota"] < 7:
            rec += 1
        else:
            reprovados += 1

print(f"Aprovados: {aprovados}")
print(f"Recuperação: {rec}")
print(f"Reprovados: {reprovados}\n")

maior_nota = alunos[0]
menor_nota = alunos[0]

for aluno in alunos:
    if aluno["nota"] > maior_nota["nota"]:
        maior_nota = aluno

    if aluno["nota"] < menor_nota["nota"]:
        menor_nota = aluno

print(f"Aluno com maior nota: {maior_nota['nome']} - ({maior_nota['nota']})")
print(f"Aluno com menor nota: {menor_nota['nome']} - ({menor_nota['nota']})")
cadastros = []
novos_alunos = True

while novos_alunos:

    while True:
        try:
            nome = input("NOME do aluno: ")
            if nome.strip():
                break
            else:
                print("Insira um NOME válido!")
        except ValueError:
            print("Insira um NOME válido!")

    while True:
        try:
            idade = int(input("IDADE do aluno: "))
            if idade > 0:
                break
            else:
                print("IDADE deve ser acima de 0!")
        except ValueError:
            print("IDADE deve ser acima de 0!")


    while True:
        try:
            nota = float(input("NOTA aluno (0 a 10): "))
            if nota > 0 and nota <= 10:
                break
            else:
                print("Insira um nota válida!")
        except ValueError:
            print("Insira notas entre 0 e 10!")

    aluno = {
    "nome": nome,
    "idade": idade,
    "nota": nota
    }

    cadastros.append(aluno)

    while True:
        resposta = input("CADASTRAR novo aluno (S/N)? ").strip().upper()

        if resposta == "S":
            novos_alunos = True
            break

        elif resposta == "N":
            novos_alunos = False
            break

        else:
            print("S ou N!")


def situacao(nota):
    if nota >= 7:
        return "Aprovado!"
    if nota >= 5 or nota <= 7:
        return "Recuperação!"
    if nota < 5:
        return "Reprovado!"
    
aluno_situacao = situacao(nota)

def media(cadastros):
    soma = 0
    for notas in cadastros:
        soma += notas["nota"]

        try:
            return soma / len(cadastros)
        except ZeroDivisionError:
            pass
    
media_turma = media(cadastros)

aprovados = 0
rec = 0
reprovados = 0

for aluno in cadastros:
    if aluno["nota"] >= 7:
        aprovados += 1
    elif aluno["nota"] >= 5 and aluno["nota"] < 7:
            rec += 1
    else:
        reprovados += 1

maior_nota = cadastros[0]
menor_nota = cadastros[0]

for notas in cadastros:
    if notas["nota"] > maior_nota["nota"]:
        maior_nota = notas

for notas in cadastros:
    if notas["nota"] < menor_nota["nota"]:
        menor_nota = notas
        
for alunos in cadastros:
    print(f"Nome: {alunos['nome']} | Idade: {aluno['idade']} | Nota: {alunos['nota']} | Situação: {aluno_situacao}")

print(f"Média turma: {media_turma}")
print(f"APROVADOS: {aprovados}")
print(f"RECUPERAÇÃO: {rec}")
print(f"REPROVADOS: {aprovados}")
print(f"MAIOR nota: {maior_nota["nome"]} - {maior_nota["nota"]}")
print(f"MENOR nota: {menor_nota["nome"]} - {menor_nota["nota"]}")
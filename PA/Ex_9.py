# informar se usuário foi aprovado:

nota = float(input("Insira sua nota: ").replace(",", "."))

if nota > 0 and nota >= 6:
    print("Você foi aprovado!")

else:
    print("Você não foi aprovado.")
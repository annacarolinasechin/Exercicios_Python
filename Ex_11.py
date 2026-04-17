# solicitar nota e determinar se aluno foi aprovado, de recuperação ou reprovado:

nota = float(input("Insira sua nota: ").replace(",", "."))

if nota >= 7:
    print("Você foi aprovado!")

elif nota >= 5 and nota < 7:
    print("Você está de recuperação!")

else:
    print("Você foi reprovado!")
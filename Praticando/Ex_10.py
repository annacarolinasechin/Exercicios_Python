# solitar 3 notas e calcular média final através de : média >= 8 = A; média >= 5 = B e média < 5 = C:

def Solicitar_Notas(mensagem):
    while True:
        try:
            return int(input(mensagem).replace(",", "."))
        except ValueError:
            print("Insira valores válidos!")

nota1 = Solicitar_Notas("Insira uma nota: ")
nota2 = Solicitar_Notas("Insira outra nota: ")
nota3 = Solicitar_Notas("Insira mais uma nota: ")

media = (nota1 + nota2+ nota3) / 3

if media >= 8:
    print(f"Sua média é: A ({media}).")

elif media >= 5:
    print(f"Sua média é: B ({media}).")

else:
    print(f"Sua média é: C ({media:.2f}).")
# usuário maior ou menor de idade:

idade = int(input("Insira sua idade: "))

if idade >= 18:
    print(f"Você é maior de idade (você tem: {idade} anos)!")

elif idade == 18:
    print("Você tem exatamente 18 anos!")

else:
    print(f"Você é menor de idade (você tem: {idade} anos)!")
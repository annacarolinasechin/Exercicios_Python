# 15) crie uma função que receba a idade de uma pessoa e retorne se ela é maior de idade ou não:

def Maior(idade):
    if idade >= 18:
        print("Você é maior de idade!")
    else:
        print("Você é menor de idade!")
    
while True:
    try:
        idade = int(input("Insira sua idade: "))
        break
    except ValueError:
        print("Insira somente valores inteiros!")

maior = Maior(idade)
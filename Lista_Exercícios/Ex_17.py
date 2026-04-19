# função que recebe idade e retorna se usuário é maior de idade: 

def Maior(idade):
    if idade >= 18:
        print("Você é maior de idade!")
    else:
        print("Você é menor de idade!")
    
idade = int(input("Insira sua idade: "))

resultado = Maior(idade)
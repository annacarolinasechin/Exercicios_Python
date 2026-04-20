# função que recebe dois valores e retorna soma: 

def Soma(n1, n2):
    return n1 + n2

def Pedir_Valores(mensagem):
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Insira valores válidos!")

n1 = Pedir_Valores("Insira um valor: ")
n2 = Pedir_Valores("Insira outro valor: ")

total = Soma(n1, n2)

print(f"A soma dos valores resulta em: {total}.")
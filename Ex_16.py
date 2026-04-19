# função que recebe dois valores e retorna soma:

def Soma(n1, n2):
    soma = n1+n2
    return soma

n1 = float(input("Insira um valor: ").replace(",", "."))
n2 = float(input("Insira outro número: ").replace(",", "."))

resultado = Soma(n1, n2)

print(f"A soma dos valores resulta em: {resultado}.")
# tratar erros de 2 valores:

while True:
    try:
        n1 = float(input("Insira um valor: "))
        break
    except ValueError:
        print("Insira um valor válido")

while True:
    try:
        n2 = float(input("Insira um valor: "))
        break
    except ValueError:
        print("Insira um valor válido")

print(f"Os valores inseridos são: {n1} e {n2}.")
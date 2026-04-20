# solicitar dois números e exibir sua soma, subtração, multiplicação e divisão entre eles:

while True:
    try:
        n1 = float(input("Insira um valor: ").replace(",", "."))
        break
    except ValueError:
        print("Insira válores válidos")

while True:
    try:
        n2 = float(input("Insira um valor: ").replace(",", "."))
        break
    except ValueError:
        print("Insira válores válidos")

print(f"A soma dos valores resulta em: {n1 + n1}")
print(f"A subtração dos valores resulta em: {n1 - n1}")
print(f"A multiplicação dos valores resulta em: {n1 * n1}")
print(f"A divião dos valores resulta em: {n1 / n1}")
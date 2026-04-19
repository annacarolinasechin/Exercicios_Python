# tratar erro caso usuário insira valor inválido: 

while True:
    try:
        valor = float(input("Insira um valor: "))
        break
    except ValueError:
        print("Insira um valor válido!")

print(f"O valor inserido é: {valor}.")
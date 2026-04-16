# solicitar ao usuário 2 números e exibir, respectivamente: a soma, subtração, multiplicação e divisão entre eles:

num1 = float(input("Insira um valor: ").replace(",", "."))
num2 = float(input("Insira outro valor: ").replace(",", "."))

print(f"A soma dos valores resulta em: {num1 + num2}.")
print(f"A subtração dos valores resulta em: {num1 - num2}.")
print(f"A multiplicação dos valores resulta em: {num1 * num2}.")
print(f"A divião dos valores resulta em: {num1 / num2}.")
# calcular a média de 3 valores inseridos pelo usuário:

num1 = float(input("Insira um valor: ").replace(",", "."))
num2 = float(input("Insira outro valor: ").replace(",", "."))
num3 = float(input("Insira mais um valor: ").replace(",", "."))

media = (num1 + num2 + num3)/3

print(f"A média dos valores inseridos resulta em: {media}.")
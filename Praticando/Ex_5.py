# Crie um programa que solicite o nome e salário atual de um jogador e se baseando nesses critérios (0 a 1000 = 20% de aumento; 
# 1000,01 a 5000 = 10%; 5000,01 pra mais = 5% ), exiba seu nome e seu novo salário:

while True:
    try:
        nome_jogador = input("Insira o nome do jogador: ")
        break
    except ValueError:
        print("Insira valores válidos!")

while True:
    try:
        salario_atual = float(input("Insira o salário atual do jogador: R$ ").replace(",", "."))
        break
    except ValueError:
        print("Insira valores válidos!")

if salario_atual <= 1000:
    salario_novo = salario_atual + salario_atual*0.20

elif salario_atual <= 5000:
    salario_novo = salario_atual + salario_atual*0.10

else:
    salario_novo = salario_atual + salario_atual*0.05

print(f"Nome do jogador: {nome_jogador};")
print(F"Salário reajustado: R${salario_novo: .2f}")
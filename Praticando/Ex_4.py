
"""
4) faça um programa que gere o preço de um veículo para o consumo final considerando
valores pagos de impostos - 45%
lucro da distribuidora - 12%

"""

valor_base = float(input("Insira o valor base do veículo: R$").replace(",", "."))

imposto = valor_base*0.45

lucro_distribuidora = valor_base*0.12

valor_total = valor_base + imposto + lucro_distribuidora

input()

print(f"Impostos (45% do valor): R${imposto};")
print(f"Lucro distribuidora (12% do valor): R${lucro_distribuidora};")
print(f"O valor total do veículo para consumo final é de: R${valor_total}.")
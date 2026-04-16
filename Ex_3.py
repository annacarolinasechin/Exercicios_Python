#  determinar o menor valor entre 3:

num1 = float(input("Insira um valor: ").replace(",", "."))
num2 = float(input("Insira outro valor: ").replace(",", "."))
num3 = float(input("Insira mais um valor: ").replace(",", "."))

if num1 < num2 and num1 < num3:
    print(f"O menor valor é: {num1}.")

if num2 < num3:
    print(f"O menor valor é: {num2}.")

else:
    print(f"O menor valor é: {num3}.")

"""
se num1 for menor que num2 e num3 = num1 é menor;
se num2 for menor que num3 = num2 é menor;
se não = num3 é o menor.
"""
# programa que recebe peso, idade, realiza cálculo do IMC e determina grau de obesidade:

while True:
    try:
        peso = float(input("Insira seu peso: ").replace(",", "."))
        break
    except ValueError:
        print("Insira valores válidos!")

while True:
    try:
        altura = float(input("Insira sua altura: ").replace(",", "."))
        break
    except ValueError:
        print("Insira valores válidos!")

IMC = peso / (altura * altura)

if IMC < 18.5:
    print(F"Abaixo do peso.")

if IMC >= 18.5 and IMC < 25:
    print("Peso normal.")

if IMC >= 25 and IMC < 30:
    print("Acima do peso.")

if IMC >= 30 and IMC < 35:
    print("Obesidade: Classe 1.")

if IMC >= 35 and IMC < 40:
    print("Obesidade: Classe 2.")

if IMC > 40:
    print("Obesidade: Classe 3.")
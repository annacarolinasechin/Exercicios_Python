"""
11) faça um programa que simule um sistema de login. 
Usuário tem até 3 tentativas para acertar a senha. 
Se acertar exiba "acesso permitido".
Caso contrário exiba "conta bloqueada"
"""

while True:
    try:
        usuario = input("Defina seu nome de usuário: @")
        break
    except ValueError:
        print("Insira um nome de usuário válido!")

while True:
    try:
        senha = int(input("Defina sua senha: "))
        break
    except ValueError:
        print("Insira somente números inteiros!")

print()

tentativas = 3

while tentativas > 0:
    user_acesso = input("Insira seu nome de usuário: @")
    user_senha = int(input("Insira sua senha: "))

    if user_acesso == usuario and user_senha == senha:
        print("Usuário e senha corretos! Acesso permitido.")
        break

    else:
        tentativas = tentativas + 1
        print(f"Senha incorreta! Restam {tentativas} tentativas.")


if tentativas == 0:
    print("Sua conta foi bloqueada!")
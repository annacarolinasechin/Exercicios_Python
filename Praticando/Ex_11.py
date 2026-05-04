tentativas = 4

while True:
    try:
        usuario = input("\nDefina seu NOME de usuário: @")
        break
    except ValueError:
        print("Insira um nome de usuário válido!")

while True:
    try:
        senha = int(input("Defina sua SENHA: "))
        break
    except ValueError:
        print("Insira somente números inteiros!")

while tentativas:
    while True:
        try:
            user_acesso = input("\nUsuário: @")
            break
        except ValueError:
            print("Insira um nome de usuário válido!")

    while True:
        try:
            user_senha = int(input("Senha: "))
            break
        except ValueError:
            print("Insira somente números inteiros!")

    if user_acesso == usuario and  user_senha == senha:
        print("\nAcesso permitido!")
        break

    else:
        tentativas -= 1
    print(f"Acesso incorreto, restam {tentativas} tentativas!")
    
    if tentativas == 0:
        print("\nConta bloqueada!")
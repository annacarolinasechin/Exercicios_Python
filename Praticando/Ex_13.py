# programa que permite o cadastro de vários usuário que ao fim, deve exibir a quantidade de usuário cadastrados e quantidade de usuários maiores de idade:

usuarios = []
continuar = True

while continuar:
    print("\n----- CADASTRO -----\n")
    nome = input("Nome: ")
    idade = int(input("Idade: "))

    novo_usuario = input("\nDeseja CADASTRAR um novo usuário (CONTINUAR/ENCERRAR)? ")

    if novo_usuario.upper() == "CONTINUAR":
        continuar = True
    else:
        continuar = False
        print("\nEncerrado!")

    cad_usuario = {
        "nome": nome,
        "idade": idade
    }

    usuarios.append(cad_usuario)


maiores = 0
for user in usuarios:
    if user["idade"] >= 18:
        maiores += 1

print("\n----- RESULTADOS -----")
print(f"\nQuantidade de usuários cadastrados: {len(usuarios)}")
print(f"Quantidade de usuários maiores de idade: {maiores}")
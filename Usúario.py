usuarios = []

while True:
    print("\n===== SISTEMA DE GERENCIAMENTO DE USUÁRIOS =====")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Excluir usuário")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do usuário: ")

        usuarios.append(nome)

        print("Usuário cadastrado com sucesso!")

    elif opcao == "2":
        print("\n===== USUÁRIOS CADASTRADOS =====")

        if len(usuarios) == 0:
            print("Nenhum usuário cadastrado.")
        else:
            for usuario in usuarios:
                print(usuario)

    elif opcao == "3":
        nome = input("Digite o nome que deseja excluir: ")

        if nome in usuarios:
            usuarios.remove(nome)
            print("Usuário excluído com sucesso!")
        else:
            print("Usuário não encontrado.")

    elif opcao == "4":
        print("Sistema encerrado!")
        break

    else:
        print("Opção inválida! Tente novamente.")

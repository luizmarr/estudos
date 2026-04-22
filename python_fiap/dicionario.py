usuarios = {}
def cadastrar_usuario(nome, email):
    if email in usuarios:
        print("Usuário já cadastrado.")
    else:
        usuarios[email] = nome
        print("Usuário cadastrado com sucesso.")

def exibir_usuarios():
    if usuarios:
        print("Usuários cadastrados:")
        for email, nome in usuarios.items():
            print(f"Nome: {nome}, Email: {email}")
    else:
        print("Nenhum usuário cadastrado.")

def remover_usuario(email):
    if email in usuarios:
        del usuarios[email]
        print("Usuário removido com sucesso.")
    else:
        print("Usuário não encontrado.")

def main():
    while True:
        print("\nMenu:")
        print("1. Cadastrar usuário")
        print("2. Exibir usuários")
        print("3. Remover usuário")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Digite o nome do usuário: ")
            email = input("Digite o email do usuário: ")
            cadastrar_usuario(nome, email)
        elif escolha == "2":
            exibir_usuarios()
        elif escolha == "3":
            email = input("Digite o email do usuário a ser removido: ")
            remover_usuario(email)
        elif escolha == "4":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
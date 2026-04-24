def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
    return conteudo

def editar_arquivo(nome_arquivo, novo_conteudo):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(novo_conteudo)

def main():
    print("Bem-vindo ao manipulador de arquivos!")
    while True:
        opção = input("Digite a opção desejada (1 - Ler arquivo, 2 - Editar arquivo, 3 - Sair): ")
        if opção == "1":
            nome_arquivo = input("Digite o nome do arquivo para ler: ")
            conteudo = ler_arquivo(nome_arquivo)
            print("Conteúdo do arquivo:")
            print(conteudo)
        elif opção == "2":
            nome_arquivo = input("Digite o nome do arquivo para editar: ")
            novo_conteudo = input("Digite o novo conteúdo para o arquivo: ")
            editar_arquivo(nome_arquivo, novo_conteudo)
            print("Arquivo editado com sucesso.")
        elif opção == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")
      
if __name__ == "__main__":    main()
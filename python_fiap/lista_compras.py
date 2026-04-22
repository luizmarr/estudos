#fazendo uma lista de compras
def adicionar_item(lista, item):
    item = input("Digite o item a ser adicionado à lista de compras: ")
    lista.append(item)
    print(f"Item '{item}' adicionado à lista de compras.")

def remover_item(lista, item):
    item = input("Digite o item a ser removido da lista de compras: ")
    if item in lista:
        lista.remove(item)
        print(f"Item '{item}' removido da lista de compras.")
    else:
        print(f"Item '{item}' não encontrado na lista de compras.")

def exibir_lista(lista):
    if lista:
        print("Lista de compras:")
        for item in lista:
            print(f"- {item}")
    else:
        print("A lista de compras está vazia.")

def main():
    lista_compras = []
    while True:
        print("\nMenu:")
        print("1. Adicionar item")
        print("2. Remover item")
        print("3. Exibir lista de compras")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_item(lista_compras, None)
        elif escolha == "2":
            remover_item(lista_compras, None)
        elif escolha == "3":
            exibir_lista(lista_compras)
        elif escolha == "4":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
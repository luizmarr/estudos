def receber_dados():
    dados_pessoa = []
    dados_pessoa.append(input("Digite o seu nome: "))
    dados_pessoa.append(int(input("Digite a sua idade: ")))
    dados_pessoa.append(input("Digite a sua cidade: "))
    return dados_pessoa

def imprimir_dados(dados):
    print(f"Nome: {dados[0]}")
    print(f"Idade: {dados[1]}")
    print(f"Cidade: {dados[2]}")

if __name__ == "__main__":
    pessoa = receber_dados()
    imprimir_dados(pessoa)
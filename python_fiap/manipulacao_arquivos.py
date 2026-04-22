class Pessoa:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def validar_dados(self):
        if not self.nome:
            print("O nome não pode ser vazio.")
            return False
        if self.idade <= 0:
            print("A idade deve ser um número positivo.")
            return False
        if not self.cidade:
            print("A cidade não pode ser vazia.")
            return False
        return True


    def receber_dados(self):
        self.nome = input("Digite o seu nome: ")

        while True:
            idade_input = input("Digite a sua idade: ")

            if idade_input.isdigit():  # verifica se é número
                self.idade = int(idade_input)
                break
            else:
                print("Digite uma idade válida (apenas números).")

        self.cidade = input("Digite a sua cidade: ") 


    def salvar_dados(self):
        with open("dados_pessoa.txt", "a") as arquivo:
            arquivo.write(f"Nome: {self.nome}\n")
            arquivo.write(f"Idade: {self.idade}\n")
            arquivo.write(f"Cidade: {self.cidade}\n")
    
   

def main():
    p = Pessoa("", 0, "")

    while True:
        p.receber_dados()
        if p.validar_dados():
            break
        print("Tente novamente.\n")

    p.salvar_dados()
    print("Dados salvos com sucesso em 'dados_pessoa.txt'.")

if __name__ == "__main__":
    main()
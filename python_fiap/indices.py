class pessoa:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def receber_dados(self):
        self.nome = input("Digite o seu nome: ")
        self.idade = int(input("Digite a sua idade: "))
        self.cidade = input("Digite a sua cidade: ")
          
    def imprimir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Cidade: {self.cidade}")
 

lista_pessoa = []
resposta = "s"
while resposta.lower() == "s":
    p = pessoa("", 0, "")
    p.receber_dados()
    lista_pessoa.append(p)
    resposta = input("Deseja adicionar outra pessoa? (s/n): ").lower()

busca = input("Digite o nome da pessoa que deseja buscar: ")
for p in lista_pessoa:
    if p.nome.lower() == busca.lower():
        p.imprimir_dados()
        encontrado = True
        break    
    else:    print("Pessoa não encontrada.")



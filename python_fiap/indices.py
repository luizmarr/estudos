pessoa = []
nome = []
cidade = []
idade = []
telefone = []

respostas = "s"

while respostas == "s":
    pessoa.append({})   
    nome.append(input("Digite o seu nome: "))
    cidade.append(input("Digite a sua cidade: "))
    idade.append(int(input("Digite a sua idade: ")))
    telefone.append(input("Digite o seu telefone: "))
    respostas = input("Deseja continuar? (s/n): ")

for i in range(len(nome)):
    pessoa[i]["nome"] = nome[i]
    pessoa[i]["cidade"] = cidade[i]
    pessoa[i]["idade"] = idade[i]
    pessoa[i]["telefone"] = telefone[i]

print(pessoa)
    

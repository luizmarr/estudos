import json
import tkinter as tk
from tkinter import messagebox  

def adicionar_gasto(categoria, valor, gastos):
    gastos.append((categoria, valor))

def calcular_total_gastos(gastos):
    total = sum(valor for categoria, valor in gastos)
    return total

def exibir_gastos(gastos):
    print("Gastos:")
    for categoria, valor in gastos:
        print(f"{categoria}: R${valor:.2f}")

def salvar_gastos(gastos, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(gastos, arquivo)
            

def carregar_gastos(nome_arquivo):
    gastos = []
    try:
        with open(nome_arquivo, 'r') as arquivo:
            gastos = json.load(arquivo)
    except FileNotFoundError:
        pass  # Se o arquivo não existir, apenas continue
    return gastos
def remover_gasto(categoria, gastos):
    gastos[:] = [gasto for gasto in gastos if gasto[0] != categoria]
def main():
    gastos = carregar_gastos("gastos.json")
    while True:
        print("\nMenu:")
        print("1. Adicionar gasto")
        print("2. Exibir gastos")
        print("3. Calcular total de gastos")
        print("4. Salvar e sair")
        print("5. Remover gasto")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            categoria = input("Digite a categoria do gasto: ")
            while True:
                try:
                    valor = float(input("Digite o valor do gasto: "))
                    break
                except ValueError:
                    print("Valor inválido. Por favor, digite um número.")
            adicionar_gasto(categoria, valor, gastos)
        elif escolha == "2":
            exibir_gastos(gastos)
        elif escolha == "3":
            total = calcular_total_gastos(gastos)
            print(f"Total de gastos: R${total:.2f}")
        elif escolha == "4":
            salvar_gastos(gastos, "gastos.json")
            print("Gastos salvos. Saindo do programa.")
            break
        elif escolha == "5":
            categoria = input("Digite a categoria do gasto a ser removido: ")
            remover_gasto(categoria, gastos)
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":    main()
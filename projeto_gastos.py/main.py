from cProfile import label
import json
import tkinter as tk
from tkinter import mainloop, messagebox  

def adicionar_gasto(categoria, valor, gastos):
    gastos.append((categoria, valor))

def calcular_total_gastos(gastos):
    total = sum(valor for categoria, valor in gastos)
    return total

def exibir_gastos(gastos):
    label_gastos.config(text="Gastos:")
    for categoria, valor in gastos:
        label_gastos.config(text=label_gastos.cget("text") + f"\n{categoria}: R${valor:.2f}")

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
    janela = tk.Tk()
    janela.title("Gerenciador de Gastos")
    label_menu = tk.Label(janela, text="Menu:")
    label_menu.pack()
    label_opcao1 = tk.Label(janela, text="1. Adicionar gasto")
    label_opcao1.pack()
    label_opcao2 = tk.Label(janela, text="2. Exibir gastos")
    label_opcao2.pack()
    label_opcao3 = tk.Label(janela, text="3. Calcular total de gastos")
    label_opcao3.pack()
    label_opcao4 = tk.Label(janela, text="4. Salvar e sair")
    label_opcao4.pack()
    label_opcao5 = tk.Label(janela, text="5. Remover gasto")
    label_opcao5.pack()
       
    escolha = entry("Escolha uma opção: ")
    if escolha == "1":
        categoria = entry("Digite a categoria do gasto: ")
        valor = float(entry("Digite o valor do gasto: "))
        adicionar_gasto(categoria, valor, gastos)
    elif escolha == "2":
        exibir_gastos(gastos)
    elif escolha == "3":
        total = calcular_total_gastos(gastos)
        messagebox.showinfo("Total de Gastos", f"O total de gastos é: R${total:.2f}")
    elif escolha == "4":
        salvar_gastos(gastos, "gastos.json")
        janela.destroy()
    elif escolha == "5":
        categoria = entry("Digite a categoria do gasto a ser removida: ")
        remover_gasto(categoria, gastos)
    else:
        messagebox.showerror("Opção inválida", "Por favor, escolha uma opção válida.")
if __name__ == "__main__":    mainloop()
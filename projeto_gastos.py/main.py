import json
import tkinter as tk
from tkinter import mainloop, messagebox  

janela = tk.Tk()
label_gastos = tk.Label(janela, text="")
label_gastos.pack()

entry_categoria = tk.Entry(janela)
entry_categoria.pack()
entry_valor = tk.Entry(janela)
entry_valor.pack()

gastos=[]
def adicionar():
    categoria = entry_categoria.get()

    try:
        valor = float(entry_valor.get())
    except ValueError:
        messagebox.showerror(
            "Erro",
            "Digite um número válido"
        )
        return

    adicionar_gasto(categoria, valor, gastos)

    entry_categoria.delete(0, tk.END)
    entry_valor.delete(0, tk.END)


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
    categoria = entry_categoria.get()
    for gasto in gastos:
        if gasto[0] == categoria:
            gastos.remove(gasto)
            messagebox.showinfo("Sucesso", f"Gasto da categoria '{categoria}' removido.")
            return

def main():
    global gastos
    gastos = carregar_gastos("gastos.json")
    janela.title("Gerenciador de Gastos")
    label_menu = tk.Label(janela, text="Menu:")
    label_menu.pack()
    label_opcao1 = tk.Label(janela, text="1. Salvar e Sair")
    label_opcao1.pack()
    label_opcao2 = tk.Label(janela, text="2. adicionar gasto")
    label_opcao2.pack()
    label_opcao3 = tk.Label(janela, text="3. exibir gastos")
    label_opcao3.pack()
    label_opcao4 = tk.Label(janela, text="4. calcular total de gastos")
    label_opcao4.pack()
    label_opcao5 = tk.Label(janela, text="5. remover gasto")
    label_opcao5.pack()
   
  
    tk.Button(janela, text="Salvar e Sair", command=lambda: salvar_gastos(gastos, "gastos.json") or janela.quit()).pack()
    tk.Button(janela, text="Adicionar Gasto", command= adicionar).pack()
    tk.Button(janela, text="Exibir Gastos", command=lambda: exibir_gastos(gastos)).pack()
    tk.Button(janela, text="Calcular Total", command=lambda: messagebox.showinfo("Total de Gastos", f"Total: R${calcular_total_gastos(gastos):.2f}")).pack()
    tk.Button(janela, text="Remover Gasto", command=lambda: remover_gasto(entry_categoria.get(), gastos)).pack()      

if __name__ == "__main__":   
    main()
    janela.mainloop()  
from tkinter import ttk
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Função para abrir a tela principal
def abrir_tela_principal():
    tela_principal = tk.Tk()
    tela_principal.title("Sistema de Contas a Pagar")
    tela_principal.geometry("600x400")

    # Criação das abas
    abas = ttk.Notebook(tela_principal)
    aba_despesas = tk.Frame(abas)
    aba_grafico = tk.Frame(abas)

    abas.add(aba_despesas, text="Despesas")
    abas.add(aba_grafico, text="Gráfico")
    abas.pack(expand=1, fill='both')

    # Aba de Despesas
    tk.Label(aba_despesas, text="Renda Mensal:").grid(row=0, column=0, padx=5, pady=5)
    renda_mensal = tk.Entry(aba_despesas)
    renda_mensal.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(aba_despesas, text="Descrição da Despesa:").grid(row=1, column=0, padx=5, pady=5)
    descricao = tk.Entry(aba_despesas)
    descricao.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(aba_despesas, text="Valor:").grid(row=2, column=0, padx=5, pady=5)
    valor = tk.Entry(aba_despesas)
    valor.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(aba_despesas, text="Mês:").grid(row=3, column=0, padx=5, pady=5)
    mes = tk.Entry(aba_despesas)
    mes.grid(row=3, column=1, padx=5, pady=5)

    # Funções para manipular despesas
    despesas = []

    def adicionar_despesa():
        despesas.append((descricao.get(), float(valor.get()), mes.get()))
        atualizar_tabela()
        atualizar_grafico()

    def atualizar_tabela():
        for widget in tabela.get_children():
            tabela.delete(widget)
        for i, desp in enumerate(despesas):
            tabela.insert('', 'end', iid=i, values=desp)

    def editar_despesa():
        selecionado = tabela.focus()
        valores = tabela.item(selecionado, 'values')
        if valores:
            descricao.delete(0, tk.END)
            descricao.insert(0, valores[0])
            valor.delete(0, tk.END)
            valor.insert(0, valores[1])
            mes.delete(0, tk.END)
            mes.insert(0, valores[2])
            despesas.pop(int(selecionado))
            atualizar_tabela()

    def excluir_despesa():
        selecionado = tabela.focus()
        if selecionado:
            despesas.pop(int(selecionado))
            atualizar_tabela()
            atualizar_grafico()

    tk.Button(aba_despesas, text="Adicionar", command=adicionar_despesa).grid(row=4, column=0, padx=5, pady=5)
    tk.Button(aba_despesas, text="Editar", command=editar_despesa).grid(row=4, column=1, padx=5, pady=5)
    tk.Button(aba_despesas, text="Excluir", command=excluir_despesa).grid(row=4, column=2, padx=5, pady=5)

    # Tabela para exibir despesas
    colunas = ("Descrição", "Valor", "Mês")
    tabela = ttk.Treeview(aba_despesas, columns=colunas, show="headings")
    tabela.heading("Descrição", text="Descrição")
    tabela.heading("Valor", text="Valor")
    tabela.heading("Mês", text="Mês")
    tabela.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

    # Aba do Gráfico
    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=aba_grafico)
    canvas.get_tk_widget().pack()

    def atualizar_grafico():
        ax.clear()
        meses = [f"{i+1:02}" for i in range(12)]
        valores_grafico = [0] * 12
        renda = float(renda_mensal.get()) if renda_mensal.get() else 0
        descricoes_por_mes = [[] for _ in range(12)]

        for desp in despesas:
            mes_idx = int(desp[2]) - 1
            valores_grafico[mes_idx] += desp[1]
            descricoes_por_mes[mes_idx].append(desp[0])

        renda_restante = [renda - val for val in valores_grafico]

        ax.plot(meses, renda_restante, marker='o')

        # Adiciona as descrições das despesas ao gráfico
        for i, (renda, descricoes) in enumerate(zip(renda_restante, descricoes_por_mes)):
            if descricoes:
                ax.text(meses[i], renda, '\n'.join(descricoes), fontsize=8, ha='center')

        ax.set_xlabel('Mês')
        ax.set_ylabel('Renda - Despesas')
        ax.set_title('Renda Mensal após Despesas')
        canvas.draw()

    tela_principal.mainloop()

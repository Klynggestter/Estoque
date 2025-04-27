import tkinter as tk
from tkinter import messagebox, ttk

# Dados armazenados em memória
produtos = []
movimentacoes = []

# Funções de lógica
def cadastrar_produto():
    try:
        id_produto = int(entry_id.get())
        nome = entry_nome.get()
        categoria = entry_categoria.get()
        quantidade = int(entry_quantidade.get())
        preco = float(entry_preco.get())
        localizacao = entry_localizacao.get()

        # Verifica se o produto já existe
        for produto in produtos:
            if produto['id_produto'] == id_produto:
                messagebox.showerror("Erro", f"Produto com ID {id_produto} já cadastrado.")
                return

        novo_produto = {
            'id_produto': id_produto,
            'nome': nome,
            'categoria': categoria,
            'quantidade': quantidade,
            'preco': preco,
            'localizacao': localizacao
        }

        produtos.append(novo_produto)
        messagebox.showinfo("Sucesso", f"Produto '{nome}' cadastrado com sucesso!")
        limpar_campos()
    except ValueError:
        messagebox.showerror("Erro", "Preencha todos os campos corretamente!")

def registrar_movimentacao():
    try:
        id_produto = int(entry_mov_id.get())
        tipo = combo_tipo.get()
        quantidade = int(entry_mov_qtd.get())
        data = entry_mov_data.get()

        produto = next((p for p in produtos if p['id_produto'] == id_produto), None)

        if not produto:
            messagebox.showerror("Erro", "Produto não encontrado.")
            return

        if tipo == "entrada":
            produto['quantidade'] += quantidade
        elif tipo == "saida":
            if produto['quantidade'] < quantidade:
                messagebox.showerror("Erro", "Quantidade insuficiente.")
                return
            produto['quantidade'] -= quantidade
        else:
            messagebox.showerror("Erro", "Tipo inválido.")
            return

        movimentacoes.append({
            'id_produto': id_produto,
            'tipo': tipo,
            'quantidade': quantidade,
            'data': data
        })

        messagebox.showinfo("Sucesso", "Movimentação registrada com sucesso!")
        entry_mov_id.delete(0, tk.END)
        entry_mov_qtd.delete(0, tk.END)
        entry_mov_data.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Erro", "Preencha os campos corretamente!")

def gerar_relatorio():
    texto = "📦 Relatório de Produtos:\n"
    for p in produtos:
        texto += (f"ID: {p['id_produto']} | Nome: {p['nome']} | Qtd: {p['quantidade']} | "
                  f"Preço: R$ {p['preco']:.2f} | Localização: {p['localizacao']}\n")
    messagebox.showinfo("Relatório de Produtos", texto)

def historico_mov():
    texto = "📑 Histórico de Movimentações:\n"
    for m in movimentacoes:
        texto += (f"Produto ID: {m['id_produto']} | Tipo: {m['tipo']} | Qtd: {m['quantidade']} | "
                  f"Data: {m['data']}\n")
    messagebox.showinfo("Histórico de Movimentações", texto)

def limpar_campos():
    entry_id.delete(0, tk.END)
    entry_nome.delete(0, tk.END)
    entry_categoria.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    entry_localizacao.delete(0, tk.END)

# Janela principal
root = tk.Tk()
root.title("Sistema de Estoque")
root.geometry("600x550")

# Cadastro de produtos
frame_cadastro = tk.LabelFrame(root, text="Cadastro de Produto", padx=10, pady=10)
frame_cadastro.pack(padx=10, pady=10, fill="x")

tk.Label(frame_cadastro, text="ID").grid(row=0, column=0)
entry_id = tk.Entry(frame_cadastro)
entry_id.grid(row=0, column=1)

tk.Label(frame_cadastro, text="Nome").grid(row=1, column=0)
entry_nome = tk.Entry(frame_cadastro)
entry_nome.grid(row=1, column=1)

tk.Label(frame_cadastro, text="Categoria").grid(row=2, column=0)
entry_categoria = tk.Entry(frame_cadastro)
entry_categoria.grid(row=2, column=1)

tk.Label(frame_cadastro, text="Quantidade").grid(row=3, column=0)
entry_quantidade = tk.Entry(frame_cadastro)
entry_quantidade.grid(row=3, column=1)

tk.Label(frame_cadastro, text="Preço").grid(row=4, column=0)
entry_preco = tk.Entry(frame_cadastro)
entry_preco.grid(row=4, column=1)

tk.Label(frame_cadastro, text="Localização").grid(row=5, column=0)
entry_localizacao = tk.Entry(frame_cadastro)
entry_localizacao.grid(row=5, column=1)

btn_cadastrar = tk.Button(frame_cadastro, text="Cadastrar Produto", command=cadastrar_produto)
btn_cadastrar.grid(row=6, columnspan=2, pady=5)

# Registro de movimentações
frame_mov = tk.LabelFrame(root, text="Movimentação", padx=10, pady=10)
frame_mov.pack(padx=10, pady=10, fill="x")

tk.Label(frame_mov, text="ID Produto").grid(row=0, column=0)
entry_mov_id = tk.Entry(frame_mov)
entry_mov_id.grid(row=0, column=1)

tk.Label(frame_mov, text="Tipo").grid(row=1, column=0)
combo_tipo = ttk.Combobox(frame_mov, values=["entrada", "saida"])
combo_tipo.grid(row=1, column=1)

tk.Label(frame_mov, text="Quantidade").grid(row=2, column=0)
entry_mov_qtd = tk.Entry(frame_mov)
entry_mov_qtd.grid(row=2, column=1)

tk.Label(frame_mov, text="Data").grid(row=3, column=0)
entry_mov_data = tk.Entry(frame_mov)
entry_mov_data.grid(row=3, column=1)

btn_movimentar = tk.Button(frame_mov, text="Registrar Movimentação", command=registrar_movimentacao)
btn_movimentar.grid(row=4, columnspan=2, pady=5)

# Relatórios
frame_relat = tk.Frame(root)
frame_relat.pack(pady=10)

btn_relatorio = tk.Button(frame_relat, text="📦 Relatório de Produtos", command=gerar_relatorio)
btn_relatorio.pack(side=tk.LEFT, padx=10)

btn_historico = tk.Button(frame_relat, text="📑 Histórico de Movimentações", command=historico_mov)
btn_historico.pack(side=tk.LEFT, padx=10)

root.mainloop()

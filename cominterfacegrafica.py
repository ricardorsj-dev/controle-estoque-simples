import tkinter as tk 
from tkinter import messagebox
import sqlite3

#Banco de dados
db = sqlite3.connect("Estoque.db") #conecta com o banco de dados
cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS produtos(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT,
               preco REAL,
               quantidade INTEGER,
               minimo INTEGER)""")
db.commit()





#função para entrada dos dados pelo usuário e adição do produto à lista
def adicionar_produto():
    nome = entry_nome.get().strip()
    preco = entry_preco.get().strip()
    quantidade = entry_quantidade.get().strip()
    minimo = entry_minimo.get().strip()

    if not nome or not preco or not quantidade or not minimo:
        messagebox.showwarning("Erro", "Preencha todos os campos")
        return
    cursor.execute("INSERT INTO produtos (nome, preco, quantidade, minimo) VALUES(?, ?, ?, ?)", 
                   (nome, float(preco), int(quantidade), int(minimo)))
    db.commit()
    atualizar_lista()
    limpar_campos()

def remover_produto():
    selecionado = lista.curselection()
    if not selecionado:
        messagebox.showwarning("Erro", "Selecione um produto!")
        return
    
    item = lista.get(selecionado)
    id_produto = item.split(" - ")[0]

    cursor.execute("DELETE FROM produtos WHERE id=?", (id_produto,))
    db.commit()
    atualizar_lista()


def vender_produto():
    selecionado = lista.curselection()

    if not selecionado:
        messagebox.showwarning("Erro", "Selecione um produto")
        return
    item = lista.get(selecionado)
    id_produto = item.split(" - ")[0]
    quantidade_venda = entry_venda.get()

    if not quantidade_venda:
        messagebox.showwarning("Erro", "Digite a quantidade vendida")
        return
    cursor.execute("SELECT quantidade FROM produtos WHERE id=?", (id_produto,))
    quantidade_atual = cursor.fetchone()[0]

    quantidade_venda = int(quantidade_venda)

    if quantidade_venda > quantidade_atual:
        messagebox.showwarning("Erro", "Estoque insuficiente")
        return
    
    nova_quantidade = quantidade_atual - quantidade_venda
    cursor.execute("UPDATE produtos SET quantidade=? WHERE id=?", (nova_quantidade, id_produto))

    db.commit()
    atualizar_lista()
    entry_venda.delete(0, tk.END)

def atualizar_lista():
    lista.delete(0, tk.END)

    cursor.execute("SELECT * FROM produtos")

    for produto in cursor.fetchall():
        id_, nome, preco, quantidade, minimo = produto

        texto = f"{id_} - {nome} - R$ {preco} - Qtd: {quantidade}"


        if quantidade <= minimo:
            texto += "⚠️ BAIXO"
        
        lista.insert(tk.END, texto)

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)
    entry_minimo.delete(0, tk.END)

#Interface
janela = tk.Tk()
janela.title("Controle de estoque")
janela.geometry("500x400")

#Frame cadastro
frame_cadastro = tk.Frame(janela)
frame_cadastro.grid(pady=10)

#Campos de preenchimento
tk.Label(frame_cadastro, text="Nome").grid(row=0, column=0)
entry_nome = tk.Entry(frame_cadastro)
entry_nome.grid(row=0, column=1)

tk.Label(frame_cadastro, text="Preço").grid(row=1, column=0)
entry_preco = tk.Entry(frame_cadastro)
entry_preco.grid(row=1, column=1)

tk.Label(frame_cadastro,text="Quantidade").grid(row=2, column=0)
entry_quantidade = tk.Entry(frame_cadastro)
entry_quantidade.grid(row=2, column=1)

tk.Label(frame_cadastro, text="Estoque mínimo").grid(row=3, column=0)
entry_minimo = tk.Entry(frame_cadastro)
entry_minimo.grid(row=3, column=1)

#Botões para interação do usuário 
tk.Button(frame_cadastro, text="Adicionar", command=adicionar_produto).grid(row=4, column=0)
tk.Button(frame_cadastro, text="Remover", command=remover_produto).grid(row=4, column=1)

#Lista 
lista = tk.Listbox(janela, width=60)
lista.grid(pady=10)

#Frame venda 
frame_venda = tk.Frame(janela)
frame_venda.grid()

tk.Label(frame_venda, text="Quantidade de venda").grid(row=0, column=0)
entry_venda = tk.Entry(frame_venda)
entry_venda.grid(row=0, column=1)

tk.Button(frame_venda, text="Vender", command=vender_produto).grid(row=0, column=2)

atualizar_lista()

janela.mainloop()


import tkinter as tk
from tkinter import ttk
import sqlite3

# Função para adicionar um novo cliente no banco de dados
def add_client():
    name = name_entry.get()
    email = email_entry.get()

    if name and email:
        conn.execute("INSERT INTO Clients (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        name_entry.delete(0, 'end')
        email_entry.delete(0, 'end')
        tel_entry.delete(0, 'end')
        load_clients()
    else:
        tk.messagebox.showwarning("Campos vazios", "Preencha todos os campos!")

# Função para carregar a lista de clientes
def load_clients():
    for row in tree.get_children():
        tree.delete(row)
    
    cursor = conn.execute("SELECT * FROM Clients")
    for row in cursor:
        tree.insert('', 'end', values=row)

# Configuração da janela principal

root =tk.Tk()
root.title("CADSTRO DE CLIENTE")
root.geometry("900x650")
root.configure(background="sky blue")


# Criação de um banco de dados SQLite e uma tabela para clientes
conn = sqlite3.connect("store.db")
conn.execute('''CREATE TABLE IF NOT EXISTS Clients
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 email TEXT NOT NULL)''')
conn.commit()

# Rótulos e entradas para nome e email
name_label = tk.Label(root, text="Nome:", font= 20)
name_label.place(x=30, y=30)
name_entry = tk.Entry(root, width=25, bd="1", font=(
            'arial 18 bold'), bg='lightgray')
name_entry.place(x=100, y=30)

email_label = tk.Label(root, text="Email:", font= 20)
email_label.place(x=30, y=70)
email_entry = tk.Entry(root, width=25, bd="1", font=(
            'arial 14 '), bg='lightgray')
email_entry.place(x=100, y=70)

tel_label = tk.Label(root, text="Telefone:", font= 20)
tel_label.place(x=30, y=140)
tel_entry = tk.Entry(root, width=25, bd="1", font=(
            'arial 18 '), bg='lightgray')
tel_entry.place(x=100, y=140)

# Botão para adicionar um novo cliente
add_button = tk.Button(root, text="Adicionar Cliente",font= 30, bg= "blue", command=add_client)
add_button.place(x=150, y=190)

# Criação de uma Treeview para exibir a lista de clientes
tree = ttk.Treeview(root, columns=("ID", "Nome", "Email"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Nome", text="Nome")
tree.heading("Email", text="Email")
tree.place(x=100, y=300)

# Carrega a lista de clientes
load_clients()

root.mainloop()

# Fechar a conexão com o banco de dados quando a janela é fechada
conn.close()


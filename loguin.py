import customtkinter as ctk
from tkinter import *
import sqlite3
from tkinter import messagebox
import subprocess as sp


class BackEnd():
    def conecta_db(self):
        self.conn = sqlite3.connect("store.db")
        self.cursor = self.conn.cursor()
        print("Conetado com sucesso")   

    def desconeta_db(self):
        self.conn.close()
        print("Banco de dados desconectado")

    def cria_tabela(self):
        self.conecta_db()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Usuarios(ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Username TEXT NOT NULL,
                Email TEXT NOT NULL,
                Senha TEXT NOT NULL,
                Confirma_Senha TEXT NOT NULL         
            );
        """) 
        self.conn.commit()
        self.desconeta_db()

    def cadastrar_usuario(self):
        self.username_cadastro = self.username_cadastro.get()
        self.email_cadastro = self.email_cadastro.get()
        self.pass_cadastro = self.pass_cadastro.get()
        self.confirma_senha = self.confirma_senha.get()

        self.conecta_db()

        self.cursor.execute("""
            INSERT INTO Usuarios(Username, Email, Senha, Confirma_Senha) VALUES (?, ?, ?, ? )""",(self.username_cadastro, self.email_cadastro, self.pass_cadastro, self.confirma_senha))

        try:
            if (self.username_cadastro == "" or self.email_cadastro == "" or self.pass_cadastro == "" or self.confirma_senha == ""):
                messagebox.showerror(title= "Sistema de Login", message="ERRO!!!\nPor favor preencha todos os campos!")             
            elif (len(self.username_cadastro) < 6):
                messagebox.showwarning(title= "Sistema de Login", message="O nome de usuário deve ser de pelo menos 6 caracteres.")
            elif (len(self.pass_cadastro) < 6):
                messagebox.showwarning(title= "Sistema de Login", message="A senha deve ter pelo menos 6 caracteres.")
            elif (self.pass_cadastro != self.confirma_senha):
                messagebox.showerror(title="Sistema de Login", message="ERRO!!!\nSenha não confere.\nDigite novamente.")
              
 
            else:
                self.conn.commit()
                messagebox.showinfo(title="Sistema de Login", message=f"Parabéns {self.username_cadastro}\nOs seus dados foram salvos com sucesso!")
                self.desconeta_db()
            self.limpa_entry_cadstro()

        except:
            self.limpa_entry_cadstro()
            messagebox.showerror(title="Sistema de Login", message="Erro no processamento do seu cadastro!\nPor favor tente novamente!")
        
            

    def verifica_login(self):
        self.username_login = self.username_entry.get()
        self.senha_login = self.pass_login_entry.get()

        self.conecta_db()
        self.cursor.execute("""
        SELECT * FROM Usuarios WHERE (Username = ? AND Senha = ?)""", (self.username_login, self.senha_login))

        self.verifica_dados = self.cursor.fetchone()#percorrendo a tabela

        try:
            if (self.username_login == "" or self.senha_login == ""):
                messagebox.showinfo(title="Sistema de Login", message="Por favor preencha todos os campos!")

            elif (self.username_login in self.verifica_dados and self.senha_login in self.verifica_dados):
                messagebox.showinfo(title="Sistema de Login", message=f"Parabéns {self.username_login}\nLogin feito com sucesso!")
                self.desconeta_db()
                self.destroy()
                sp.run(["python","finan.py"],)
        except:
            messagebox.showerror(title="Sistema de Login", message="ERRO!!!\nDados não encontrados.\nPor favor verifique seus dados ou se cadastre.")
            self.desconeta_db()


class App(ctk.CTk, BackEnd):
    def __init__(self):
        super().__init__()
        self.configuracoes_de_janela_inicial()
        self.tela_de_login()
        self.tema()
        self.tela_de_login()
        self.cria_tabela()
           

    #configurando a janela pricipal
    def configuracoes_de_janela_inicial(self):
        self.geometry("350x400")
        self.title("Sistema de Login")
        self.resizable(False, False)

    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def tela_de_login(self):
        
        #Criar frame do formulário de login
        self.frame_login = ctk.CTkFrame(self, width=350, height=380)
        self.frame_login.place(x=10, y=10)

        #Colocando widgets dentro do frame - Formulario de login
        self.lb_tittle = ctk.CTkLabel(self.frame_login, text="Faça o seu Login",font=("Century Gothic bold", 30),corner_radius=12)
        self.lb_tittle.grid(row=0, column=0, pady=10, padx=5)

        self.username_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Seu nome de Usuário...", font=("Century gothic bold",16),corner_radius=15)
        self.username_entry.grid(row=2, column=0, pady=10, padx=5)

        self.pass_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Digite sua senha.", font=("Century gothic bold",16),corner_radius=15, show="*")
        self.pass_login_entry.grid(row=3, column=0, pady=10, padx=5)

        self.ver_senha = ctk.CTkCheckBox(self.frame_login, text="Click para ver a Senha...", font=("Century gothic bold",12),corner_radius=1)
        self.ver_senha.grid(row=4, column=0, pady=10, padx=5)

        self.btn_login = ctk.CTkButton(self.frame_login, width=300, text="Fazer Login".upper(), font=("Century gothic bold",16),corner_radius=15, command=self.verifica_login)
        self.btn_login.grid(row=5, column=0, pady=10, padx=5)

        self.span = ctk.CTkLabel(self.frame_login, text="Se não tem conta,\n click abaixo para cadastrar no Sistema!", font=("Century Gothic", 17))
        self.span.grid(row=6, column=0, pady=10, padx=5)

        self.btn_login = ctk.CTkButton(self.frame_login, width=300, fg_color="#050",hover_color="#050", text="Fazer Cadastro".upper(), font=("Century gothic bold",16), corner_radius=20, command=self.tela_de_cadastro)
        self.btn_login.grid(row=7, column=0, pady=10, padx=5)

    def tela_de_cadastro(self):
        #remover o formulário de login
        self.frame_login.place_forget()
        #Frame cadastro
        self.frame_cadastro = ctk.CTkFrame(self, width=350, height=380)
        self.frame_cadastro.place(x=10, y=10)

        #Criando o título
        self.lb_tittle = ctk.CTkLabel(self.frame_cadastro, text="Faça o seu Login",font=("Century Gothic bold", 22),corner_radius=15)
        self.lb_tittle.grid(row=0, column=0, padx=10, pady=10)

         #Criar wigets da tela de cadastro
        self.username_cadastro = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Seu nome de Usuário...", font=("Century gothic bold",16),corner_radius=15)
        self.username_cadastro.grid(row=1, column=0, padx=10, pady=10)

        self.email_cadastro = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Email do Usuário...", font=("Century gothic bold",14),corner_radius=15)
        self.email_cadastro.grid(row=2, column=0, padx=10, pady=10)

        self.pass_cadastro = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Senha de usuário.", font=("Century gothic bold",14),corner_radius=15, show="*")
        self.pass_cadastro.grid(row=3, column=0, padx=10, pady=10)

        self.confirma_senha= ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Confirme a Senha.", font=("Century gothic bold",14),corner_radius=15,show="*")
        self.confirma_senha.grid(row=4, column=0, padx=10, pady=10)

        self.ver_senha = ctk.CTkCheckBox(self.frame_cadastro, text="Click para ver a Senha...", font=("Century gothic bold",12),corner_radius=15)
        self.ver_senha.grid(row=5, column=0, padx=10)

        self.btn_cadastrar_user = ctk.CTkButton(self.frame_cadastro, width=300, fg_color="#050",hover_color="#050", text="Fazer Cadastro".upper(), command=self.cadastrar_usuario, font=("Century gothic bold",14), corner_radius=20)
        self.btn_cadastrar_user.grid(row=6, column=0, padx=10, pady=10)

        self.btn_login_back= ctk.CTkButton(self.frame_cadastro, width=300, text="Voltar ao Login".upper(), font=("Century gothic bold",14),corner_radius=20, fg_color="#444", hover_color="#333", command=self.tela_de_login)
        self.btn_login_back.grid(row=7, column=0, padx=10, pady=10)
        


    def limpa_entry_cadstro(self):
        self.str('username_cadastro').delete(0, END)
        self.email_entry.delete(0, END)
        self.pass_cadastro.delete(0, END)
        self.confirma_senha.delete(0, END)

    def limpa_entry_login(self):
        self.username_entry.delete(0, END)
        self.pass_login_entry.delete(0, END)

    def fechar_tela(self):
        self.tela_de_login.destroy()
                 

if __name__=="__main__":
    app = App()
    app.mainloop()


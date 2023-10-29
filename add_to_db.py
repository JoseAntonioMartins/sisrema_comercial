from tkinter import *
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect("store.db")
c = conn.cursor()

result = c.execute("SELECT Max(id) from inventory")
for r in result:
    id = r[0]

class Database:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.heading = Label(master, text="Cadastros De Produtos", font=('arial 40 bold'), fg='white', bg='cornflowerblue')
        self.heading.place(x=400,y=0)  

        self.name_1 = Label(master, text="Produto: ", font=('arial 18 bold'), bg='cornflowerblue')
        self.name_1.place(x=0,y=70)

        self.stock_1 = Label(master, text="Estoque: ", font=('arial 18 bold'), bg='cornflowerblue')
        self.stock_1.place(x=0,y=120)

        self.cp_1 = Label(master, text="Preço Custo: ", font=('arial 18 bold'), bg='cornflowerblue')
        self.cp_1.place(x=0,y=170)

        self.sp_1 = Label(master, text="Preço Venda: ", font=('arial 18 bold'), bg='cornflowerblue')
        self.sp_1.place(x=0,y=220)

        self.vendor_1 = Label(master, text="Fornecedor: ", font=('arial 18 bold'), bg='cornflowerblue')
        self.vendor_1.place(x=0,y=270)

        self.vender_phone_1 = Label(master, text="Tel. Fornecedor: ", font=('arial 18 bold'), bg='cornflowerblue')
        self.vender_phone_1.place(x=0,y=320)

        self.id = Label(master, text="ID: ", font=('arial 18 bold'), bg='cornflowerblue')
        self.id.place(x=0,y=370)

        self.name_e = Entry(master, width= 25, font=('arial 18 bold'))
        self.name_e.place(x=380,y=70)

        self.stock_e = Entry(master, width= 25, font=('arial 18 bold'))
        self.stock_e.place(x=380,y=120)

        self.cp_e = Entry(master, width= 25, font=('arial 18 bold'))
        self.cp_e.place(x=380,y=170)

        self.sp_e = Entry(master, width= 25, font=('arial 18 bold'))
        self.sp_e.place(x=380,y=220)

        self.vendor_e = Entry(master, width= 25, font=('arial 18 bold'))
        self.vendor_e.place(x=380,y=270)

        self.vendor_phone_e = Entry(master, width= 25, font=('arial 18 bold'))
        self.vendor_phone_e.place(x=380,y=320)

        self.id_e = Entry(master, width= 25, font=('arial 18 bold'))
        self.id_e.place(x=380,y=370)

        self.btn_add = Button(master, text="Cadastrar",font=('arial 10 bold'), width= 25, height=2, bg='steelblue',fg='black',command=self.get_items)
        self.btn_add.place(x=520,y=420)
   
        self.btn_clear = Button(master, text="Limpar", font=('arial 10 bold'), width= 18, height=2,bg='orange',fg='black', command=self.clear_all)
        self.btn_clear.place(x=380,y=420)

        self.tBox = Text(master, width= 60,height=18, bg='lightyellow')
        self.tBox.place(x=750,y=70)
        self.tBox.insert(END, "Ultimo Cadasto ID: " + str(id))

        self.master.bind('<Return>',self.get_items)
        self.master.bind('<Up>',self.clear_all)

    def get_items(self, *args, **kwargs):
        self.name = self.name_e.get()
        self.stock = self.stock_e.get()
        self.cp = self.cp_e.get()
        self.sp = self.sp_e.get()
        self.vendor= self.vendor_e.get()
        self.vendor_phone = self.vendor_phone_e.get()
        
        self.totalcp = float(self.cp) * float(self.stock)
        self.totalsp = float(self.sp) * float(self.stock)

        self.assumed_profit = float(self.totalsp - self.totalcp)

        if self.name =='' or self.stock =='' or self.cp =='' or self.sp=='':
            tkinter.messagebox.showinfo("Diasmelhores79@gmail.com","FAVOR PREENCHER TODOS OS CAMPOS.")
        else:
            sql = "INSERT INTO inventory(name, stock, cp, sp, totalcp, totalsp, assumed_profit, vendor, vendor_phoneno) VALUES(?,?,?,?,?,?,?,?,?)"
            c.execute(sql,(self.name, self.stock, self.cp, self.sp, self.totalcp, self.totalsp, self.assumed_profit, self.vendor, self.vendor_phone))
            conn.commit()
            self.tBox.insert(END,"\n\nCadastrou\n" + str(self.name) + "\nNo Banco De Dados com ID" + str(self.id_e.get()))

            tkinter.messagebox.showinfo("Diasmelhores79@gmail.com","CADASTRO REALIZADO COM SUCESSO.")
            
    def clear_all(self, *args, **kwargs):
        num = id + 1
        self.name_e.delete(0, END)
        self.stock_e.delete(0, END)
        self.cp_e.delete(0, END)
        self.sp_e.delete(0, END)
        self.vendor_e.delete(0, END)
        self.vendor_phone_e.delete(0, END)
        #self.id_e.delete(0, END)

root = Tk()
b = Database(root)
root.geometry("1366x768+0+0")
root.title("FORMULARIO DE CADASTRO")
root.configure(background='cornflowerblue')
root.mainloop()                                                                          

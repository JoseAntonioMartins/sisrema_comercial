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
        self.heading = Label(master, text="Atualização De Produtos", font=(
            'arial 40 bold'), fg='steelblue',bg='lightgreen')
        self.heading.place(x=400, y=0)

        self.id = Label(
            master, text="Digite o Código do Produto: ", font=('arial 18 bold'),bg='lightgreen')
        self.id.place(x=0, y=70)

        self.id_leb = Entry(master, width=10, font=('arial 18 bold'))
        self.id_leb.place(x=380, y=70)

        self.btn_search = Button(master, text="Pesquisar", font=(
            'arial 10 bold'), width=15, height=1, bg='orange', fg='black', command=self.search)
        self.btn_search.place(x=520, y=70)

        self.name_1 = Label(master, text="Produto: ", font=('arial 18 bold'),bg='lightgreen')
        self.name_1.place(x=0, y=120)

        self.stock_1 = Label(master, text="Estoque: ", font=('arial 18 bold'),bg='lightgreen')
        self.stock_1.place(x=0, y=170)

        self.cp_1 = Label(master, text="Preço Custo: ",
                          font=('arial 18 bold'),bg='lightgreen')
        self.cp_1.place(x=0, y=220)

        self.sp_1 = Label(master, text="Preço Venda: ",
                          font=('arial 18 bold'),bg='lightgreen')
        self.sp_1.place(x=0, y=270)

        self.totalcp_1 = Label(master, text="Total Preço Custo: ",
                          font=('arial 18 bold'),bg='lightgreen')
        self.totalcp_1.place(x=0, y=320)

        self.totalsp_1 = Label(master, text="Total Preço Venda: ",
                          font=('arial 18 bold'),bg='lightgreen')
        self.totalsp_1.place(x=0, y=370)

        self.vendor_1 = Label(master, text="Fornecedor: ",
                              font=('arial 18 bold'),bg='lightgreen')
        self.vendor_1.place(x=0, y=420)

        self.vender_phone_1 = Label(
            master, text="Tel. Fornecedor: ", font=('arial 18 bold'),bg='lightgreen')
        self.vender_phone_1.place(x=0, y=470)

        self.name_e = Entry(master, width=25, font=('arial 18 bold'))
        self.name_e.place(x=380, y=120)

        self.stock_e = Entry(master, width=25, font=('arial 18 bold'))
        self.stock_e.place(x=380, y=170)

        self.cp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.cp_e.place(x=380, y=220)

        self.sp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.sp_e.place(x=380, y=270)

        self.totalcp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.totalcp_e.place(x=380, y=320)

        self.totalsp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.totalsp_e.place(x=380, y=370)

        self.vendor_e = Entry(master, width=25, font=('arial 18 bold'))
        self.vendor_e.place(x=380, y=420)

        self.vendor_phone_e = Entry(master, width=25, font=('arial 18 bold'))
        self.vendor_phone_e.place(x=380, y=470)

        self.btn_add = Button(master, text="Atualizar", font=(
            'arial 10 bold'), width=20, height=2, bg='steelblue', fg='black', command=self.update)
        self.btn_add.place(x=520, y=520)

        self.btn_clear = Button(master, text="Limpar", font=(
            'arial 10 bold'), width=18, height=2, bg='orange', fg='black')
        self.btn_clear.place(x=380, y=520)

        self.tBox = Text(master, width=60, height=18,bg='lightyellow')
        self.tBox.place(x=750, y=70)
        self.tBox.insert(END, "Ultimo Cadasto ID: " + str(id))

    def search(self, *args, **kargs):
        sql = "SELECT *FROM inventory WHERE id=?"
        result = c.execute(sql, (self.id_leb.get(),))
        for r in result:
            self.n1 = r[1]
            self.n2 = r[2]
            self.n3 = r[3]
            self.n4 = r[4]
            self.n5 = r[5]
            self.n6 = r[6]
            self.n7 = r[7]
            self.n8 = r[8]
            self.n9 = r[9]
        conn.commit()
        self.name_e.delete(0, END)
        self.name_e.insert(0, str(self.n1))

        self.stock_e.delete(0, END)
        self.stock_e.insert(0, str(self.n2))

        self.cp_e.delete(0, END)
        self.cp_e.insert(0, str(self.n3))

        self.sp_e.delete(0, END)
        self.sp_e.insert(0, str(self.n4))

        self.vendor_e.delete(0, END)
        self.vendor_e.insert(0, str(self.n8))

        self.vendor_phone_e.delete(0, END)
        self.vendor_phone_e.insert(0, str(self.n9))

        self.totalcp_e.delete(0, END)
        self.totalcp_e.insert(0, str(self.n5))

        self.totalsp_e.delete(0, END)
        self.totalsp_e.insert(0, str(self.n6))
    
    def update(self, *args, **kargs):
        self.u1 = self.name_e.get()
        self.u2 = self.stock_e.get()
        self.u3 = self.cp_e.get()
        self.u4 = self.sp_e.get()
        self.u5 = self.totalcp_e.get()
        self.u6 = self.totalsp_e.get()
        self.u7 = self.vendor_e.get()
        self.u8 = self.vendor_phone_e.get()

        query = "UPDATE inventory SET name=? , stock=? , cp=? , sp=? , totalcp=? , totalsp=? , vendor=? , vendor_phoneno=? WHERE id=?"
        c.execute(query, (self.u1, self.u2, self.u3, self.u4, self.u5, self.u6, self.u7, self.u8, self.id_leb.get()))
        conn.commit()
        tkinter.messagebox.showinfo("Diasmelhores@gmail.com","Atualizado com Sucesso")

    

root = Tk()
b = Database(root)

root.geometry("1366x768+0+0")
root.title("ATUALIZÇÃO DE CADASTRO")
root.configure(background='lightgreen')
root.mainloop()

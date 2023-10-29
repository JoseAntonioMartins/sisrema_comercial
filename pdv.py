from tkinter import *
import tkinter.messagebox
import sqlite3
import datetime

# Importando módulos para impressão
import win32print
import win32ui

conn = sqlite3.connect("store.db")
c = conn.cursor()

date = datetime.datetime.now().date()

products_list = []
product_price = []
product_quantity = []
product_id = []


class Application:
    def __init__(self, master, *args, **kwargs):
        self.master = master

        self.left = Frame(master, width=700, height=768, bg='white')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=666, height=768, bg='lightblue')
        self.right.pack(side=RIGHT)

        self.heading = Label(self.left, text="Supermercado: ",
                             font=('arial 40 bold'), bg='lightblue')
        self.heading.place(x=20, y=0)

        self.date_1 = Label(self.right, text="Data de Hoje: " + str(date),
                            font=('arial 16 bold'), bg='lightblue')
        self.date_1.place(x=0, y=0)

        self.tproduct = Label(self.right, text="Produto : ",
                              font=('arial 18 bold'), bg='lightblue', fg='white')
        self.tproduct.place(x=0, y=60)

        self.tquantity = Label(self.right, text="Quantidade : ",
                               font=('arial 18 bold'), bg='lightblue', fg='white')
        self.tquantity.place(x=300, y=60)

        self.tamount = Label(self.right, text="Valor : ",
                             font=('arial 18 bold'), bg='lightblue', fg='white')
        self.tamount.place(x=500, y=60)

        self.enterid = Label(self.left, text="Código Produto : ",
                             font=('arial 18 bold'), bg='White')
        self.enterid.place(x=0, y=160)

        self.enteride = Entry(self.left, width=20, bd="1", font=(
            'arial 18 bold'), bg='lemonchiffon')
        self.enteride.place(x=200, y=160)

        self.search_btn = Button(self.left, text="Pesquisar Produto", command=self.search_product, font=(
            'arial 10 bold'), width=22, height=2, bg='royalblue', fg='black')
        self.search_btn.place(x=470, y=162)

        # Cliente
        self.cliente_lb = Label(self.left, text="Nome do Cliente: ",
                                font=('arial 14 bold'), bg='White')
        self.cliente_lb.place(x=0, y=78)

        self.ent_cliente = Entry(self.left, width=20, bd="1", font=(
            'arial 18 bold'), bg='lemonchiffon')
        self.ent_cliente.place(x=200, y=75)

        self.cliente_btn = Button(self.left, text="Buscar Cliente", command=self.search_client, font=(
            'arial 10 bold'), width=22, height=2, bg='green', fg='black')
        self.cliente_btn.place(x=470, y=75)

        self.customer_name = Label(self.left, text="Nome do Cliente: ", font=(
            'arial 18 bold'), bg='white')
        self.customer_name.place(x=0, y=120)

        self.total_1 = Label(self.right, text="Preço Total : ", font=(
            'arial 40 bold'), bg='lightblue', fg='black')
        self.total_1.place(x=0, y=560)

        self.productname = Label(self.left, text="", font=(
            'arial 40 bold'), bg='White', fg='green')
        self.productname.place(x=10, y=200)

        self.pprice = Label(self.left, text="", font=(
            'arial 60 bold'), fg='black')
        self.pprice.place(x=10, y=260)

        self.quantity_1 = Label(self.left, text="Quantidade :",
                                font=('arial 22 bold'), bg='white')
        self.quantity_1.place(x=0, y=370)

        self.quantity_e = Entry(self.left, width=25, bd="1", font=(
            'arial 18 bold'), bg='lightgray')
        self.quantity_e.place(x=190, y=370)
        self.quantity_e.focus()

        self.discount_1 = Label(self.left, text="Desconto :",
                                font=('arial 18 bold'), bg='white')
        self.discount_1.place(x=0, y=410)

        self.discount_e = Entry(self.left, width=25, bd="0", font=(
            'arial 18 bold'), bg='lightgray')
        self.discount_e.place(x=190, y=410)
        self.discount_e.insert(END, 0)

        self.cart_btn = Button(self.left, text="Carrinho", command=self.add_to_cart, font=(
            'arial 12 bold'), width=20, height=2, bg='royalblue', fg='black')
        self.cart_btn.place(x=350, y=450)

        self.change_1 = Label(self.left, text="Total Pago :",
                              font=('arial 18 bold'), bg='white')
        self.change_1.place(x=0, y=550)

        self.change_e = Entry(self.left, width=25, bd="0",
                              font=('arial 12 bold'), bg='bisque')
        self.change_e.place(x=190, y=550)

        self.change_btn = Button(self.left, text="Troco", command=self.calculate_change, font=(
            'arial 12 bold'), width=20, height=2, bg='tomato', fg='black')
        self.change_btn.place(x=350, y=590)

        self.Gerarrec_btn = Button(self.left, text="Recibo", command=self.generate_receipt, font=(
            'arial 12 bold'), width=20, height=2, bg='yellow', fg='black')
        self.Gerarrec_btn.place(x=350, y=640)

    def search_product(self):
        product_id = self.enteride.get()
        query = "SELECT name, sp, stock FROM inventory WHERE id=?"
        result = c.execute(query, (product_id,))

        for row in result:
            self.get_name = row[0]
            self.get_price = row[1]
            self.get_stock = row[2]

        self.productname.configure(text=str(self.get_name))
        self.pprice.configure(text="Preço : R$" + str("%.2f" % (self.get_price)))

        self.quantity_1 = Label(self.left, text="Quantidade :",
                                font=('arial 22 bold'), bg='white')
        self.quantity_1.place(x=0, y=370)

        self.quantity_e = Entry(self.left, width=25, bd="1", font=(
            'arial 18 bold'), bg='lightgray')
        self.quantity_e.place(x=190, y=370)
        self.quantity_e.focus()

        self.discount_1 = Label(self.left, text="Desconto :",
                                font=('arial 18 bold'), bg='white')
        self.discount_1.place(x=0, y=410)

        self.discount_e = Entry(self.left, width=25, bd="0", font=(
            'arial 18 bold'), bg='lightgray')
        self.discount_e.place(x=190, y=410)
        self.discount_e.insert(END, 0)

        self.cart_btn = Button(self.left, text="Carrinho", command=self.add_to_cart, font=(
            'arial 12 bold'), width=20, height=2, bg='royalblue', fg='black')
        self.cart_btn.place(x=350, y=450)

        self.change_1 = Label(self.left, text="Total Pago :",
                              font=('arial 18 bold'), bg='white')
        self.change_1.place(x=0, y=550)

        self.change_e = Entry(self.left, width=25, bd="0",
                              font=('arial 12 bold'), bg='bisque')
        self.change_e.place(x=190, y=550)

        self.change_btn = Button(self.left, text="Troco", command=self.calculate_change, font=(
            'arial 12 bold'), width=20, height=2, bg='tomato', fg='black')
        self.change_btn.place(x=350, y=590)

        self.Gerarrec_btn = Button(self.left, text="Recibo", command=self.generate_receipt, font=(
            'arial 12 bold'), width=20, height=2, bg='yellow', fg='black')
        self.Gerarrec_btn.place(x=350, y=640)

    def search_client(self):
        client_id = self.ent_cliente.get()
        query = "SELECT name FROM Clients WHERE id = ?"
        result = c.execute(query, (client_id,))
        cliente = c.fetchone()

        if cliente is not None:
            self.customer_name.configure(text="Nome do Cliente: " + cliente[0])
        else:
            tkinter.messagebox.showinfo('Erro', 'Cliente não encontrado')

    def add_to_cart(self):
        quantity_value = int(self.quantity_e.get())
        if quantity_value > self.get_stock:
            tkinter.messagebox.showinfo(
                "Supermercado", "QUANTIDADE ACIMA DO ESTOQUE!")
        else:
            final_price = (float(quantity_value) * float(self.get_price)) - (float(self.discount_e.get()))
            products_list.append(self.get_name)
            product_price.append(final_price)
            product_quantity.append(quantity_value)
            product_id.append(self.enteride.get())

            self.x_index = 0
            self.y_index = 100
            self.counter = 0

            for product in products_list:
                tempname = Label(self.right, text=str(products_list[self.counter]), font=('arial 18 bold'), bg='lightblue', fg='black')
                tempname.place(x=0, y=self.y_index)

                tempqt = Label(self.right, text=str(product_quantity[self.counter]), font=('arial 18 bold'), bg='lightblue', fg='black')
                tempqt.place(x=300, y=self.y_index)

                tempprice = Label(self.right, text="R$"+str("%.2f" % product_price[self.counter]), font=('arial 18 bold'), bg='lightblue', fg='black')
                tempprice.place(x=480, y=self.y_index)

                self.y_index += 40
                self.counter += 1

            self.total_1.configure(text="Total: R$"+str("%.2f" % sum(product_price)))
            self.quantity_1.place_forget()
            self.quantity_e.place_forget()
            self.discount_1.place_forget()
            self.discount_e.place_forget()
            self.productname.configure(text="")
            self.pprice.configure(text="")
            self.cart_btn.destroy()
            self.enteride.focus()
            self.enteride.delete(0, END)

    def calculate_change(self):
        amount_given = float(self.change_e.get())
        our_total = float(sum(product_price))
        to_give = amount_given - our_total
        c_amount = Label(self.right, text="Troco: R$"+str("%.2f" % to_give), font=('arial 30 bold'), bg='white', fg='red')
        c_amount.place(x=10, y=640)

    def generate_receipt(self):
        cliente = self.customer_name.cget("text").replace("Nome do Cliente: ", "")
        produto = self.enteride.get()
        valor = float(sum(product_price))

        if not cliente or not produto:
            tkinter.messagebox.showwarning("Campos vazios", "Por favor, selecione um cliente e produto.")
            return

        recibo = f"Recibo de Venda  \n\nCliente: {cliente} \nProduto: {produto} \n(Valor: R$ {valor:.2f}"

        # Impressão direta
        printer_name = win32print.GetDefaultPrinter()
        hprinter = win32print.OpenPrinter(printer_name)
        printer_info = win32print.GetPrinter(hprinter, 3)
        
        hdc = win32ui.CreateDC()
        hdc.CreatePrinterDC(printer_name)
        hdc.StartDoc("Recibo")
        hdc.StartPage()

        # Defina a fonte e as coordenadas de início de impressão
        hdc.TextOut(100, 100, recibo)

        hdc.EndPage()
        hdc.EndDoc()
        hdc.DeleteDC()

        tkinter.messagebox.showinfo("Recibo Impresso", "O recibo foi impresso na impressora padrão.")

        # Limpar os campos após gerar o recibo
        self.ent_cliente.delete(0, END)
        self.enteride.delete(0, END)
        self.customer_name.configure(text="Nome do Cliente: ")
        self.productname.configure(text="")
        self.pprice.configure(text="")
        self.total_1.configure(text="Preço Total : ")


root = Tk()
b = Application(root)
root.geometry("1366x768+0+0")
root.title("AREA DE VENDAS")
root.mainloop()


import sqlite3
from tkinter import *
from tkinter import Tk, ttk
import subprocess as sp
from tkcalendar import Calendar, DateEntry
from datetime import date
from tkinter.ttk import Progressbar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from tkinter import messagebox
import pandas as pd

#criando conexão
conn = sqlite3.connect("store.db")
#---------------------------------------------------------------------
# Criando tabelas categorias                                      
with conn:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Categoria(id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT)""") 

# Criando tabela receitas                                      
with conn:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Receitas(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, adicionado DATE, valor DECIMAL)""")

  
 # Criando  tabela despesas                                      
with conn:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Despesas(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, retirado_em DATE, valor INTEGER)""") 

#-----------------------------------------------------------------------
# Inserindo dados
def inserir_categoria(i):
    with conn:
        cursor = conn.cursor()
        query = "INSERT INTO Categoria (nome) VALUES (?)"
        cursor.execute(query, i)

#Criando Receitas     
def inserir_receitas(i):
        with conn:
            cursor = conn.cursor()
            query = "INSERT INTO Receitas (Categoria, adicionado, valor) VALUES (?,?,?)"
            cursor.execute(query, i)  

#Criando Despesas
def inserir_despesas(i):
        with conn:
            cursor = conn.cursor()
            query = "INSERT INTO Despesas (Categoria, retirado_em, valor) VALUES (?,?,?)"
            cursor.execute(query,i)

#-------------------------------------------------------------------------------
################# Função Deletar ###############
# Deletar Receitas
def deletar_receitas(i):
    with conn:
            cursor = conn.cursor()
            query = "DELETE FROM Receitas WHERE id=?"
            cursor.execute(query, i) 

# Deletar Despesas
def deletar_despesas(i):
    with conn:
            cursor = conn.cursor()
            query = "DELETE FROM Despesas WHERE id=?"
            cursor.execute(query, i) 


################# Funções para ver dados ###############

#Ver categoria
def ver_categoria():
    lista_itens = []

    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Categoria")
        linha = cursor.fetchall() 
        for l in linha:
            lista_itens.append(l)

    return lista_itens

#Ver receitas
def ver_receitas():
    lista_itens = []

    with conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Receitas") 
                linha = cursor.fetchall() 
                for l in linha:
                    lista_itens.append(l)

    return lista_itens

    #Ver despesas
def ver_despesas():
    lista_itens = []

    with conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Despesas")
                linha = cursor.fetchall()  
                for l in linha:
                    lista_itens.append(l)

    return lista_itens

#---------------------------------------------------------------------------------
################# Tabela Renda mensal  ##########
def tabela():
    gastos = ver_despesas()
    receitas = ver_receitas()

    tabela_lista = []

    for i in gastos:
        tabela_lista.append(i)

    for i in receitas:
        tabela_lista.append(i)

    return tabela_lista

#-------------------------------------------------------------------
def bar_valores():
    # Receita Total ------------------------
    receitas = ver_receitas()
    receitas_lista = []

    for i in receitas:
        receitas_lista.append(i[3])

    receita_total = sum(receitas_lista)

    # Despesas Total ------------------------
    gastos = ver_despesas()
    gastos_lista = []

    for i in gastos:
        gastos_lista.append(i[3])

    gastos_total = sum(gastos_lista)
    

    #Saldo Total ------------------------
    saldo_total = receita_total - gastos_total

    return[receita_total,gastos_total,saldo_total]
 

#---------------------------------------------------------------------
# Fuçao grafico pie
def pie_valores():
    gastos = ver_despesas()
    tabela_lista = []

    for i in gastos:
        tabela_lista.append(i)

    dataframe = pd.DataFrame(tabela_lista,columns = ['id', 'categoria', 'Data', 'valor'])

    # Get the sum of the durations per month
    dataframe = dataframe.groupby('categoria')['valor'].sum()
   
    lista_quantias = dataframe.values.tolist()
    lista_categorias = []

    for i in dataframe.index:
        lista_categorias.append(i)

    return([lista_categorias,lista_quantias])

#-----------------------------------------------------------------------
#percentagen
def percentagem_valor(total):
    # Receita Total ------------------------
    receitas = ver_receitas()
    receitas_lista = []

    for i in receitas:
        receitas_lista.append(i[3])

    receita_total = sum(receitas_lista)
    pass
    # Despesas Total ------------------------
    despesas = ver_despesas()
    despesas_lista = []

    for i in despesas:
        despesas.append(i[3])

    despesas_total = sum(despesas_lista)

    # Percentagem total Total ------------------------
    total = ((receita_total - despesas_total) / receita_total) * 100

    return (total)


#---------------------------------------------------------------------------------

################# cores ###############
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#3fbfb9"   # verde
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde
colors = ['#5588bb', '#66bbbb','#99bb55', '#ee9944', '#444466', '#bb5555']

################# criando janela ###############
janela = Tk()
janela.title("FINANCEIRO")
janela.geometry("1200x650")
janela.configure(background="sky blue")
janela.resizable(width=FALSE, height=FALSE)
style = ttk.Style(janela)
style.theme_use("clam")

################# criando frames divisão de janelas ###############

frameCima = Frame(janela, width=1200, height=50,bg="green", relief="flat")
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1200, height=361,bg='white',pady=20,relief='raised')
frameMeio.grid(row=1, column=0,pady=1,padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1200, height=300,bg='white',relief='flat')
frameBaixo.grid(row=2, column=0,pady=0,padx=10, sticky=NSEW)

################# Trabalhando framesCima ###############
app_logo = Label(frameCima, text="Controle Financeiro",width=900, compound=LEFT,anchor=NW, font=("Verdana", 30, 'bold'), bg='White',fg="#403d3d")
app_logo.place(x=2,y=0)

################# Atalhos para outras telas ###############
def pdv():
        sp.run(["python","pdv.py"])

def add():
        sp.run(["python","add_to_db.py"])

def cadastro():
        sp.run(["python","clientes.py"])


chamar_telas = Label(frameMeio, text="Setores da Empresa",width=90, compound=LEFT,anchor=NW, font=("Verdana", 14, 'bold','italic', 'underline'), bg='white',fg="#403d3d")
chamar_telas.place(x=900,y=0)

cadastro_clientes = Label(frameMeio, text="Cadastro de Clientes",width=90, compound=LEFT,anchor=NW, font=("Verdana", 12, 'bold'), bg='white',fg="#403d3d")
cadastro_clientes.place(x=950,y=55)

botao_cliente = Button(frameMeio, compound=RIGHT, text="Clientes".upper(), command=cadastro, width=10, font=('Ivy 12 bold'),bg="red", fg="white" )
botao_cliente.place(x=950, y=90)
#-------------------------------------
tela_vendas = Label(frameMeio, text="Vendas",width=90, compound=LEFT,anchor=NW, font=("Verdana", 12, 'bold'), bg='white',fg="#403d3d")
tela_vendas.place(x=950,y=145)

botao_pdv = Button(frameMeio, compound=RIGHT, text="PDV".upper(), command=pdv, width=10, font=('Ivy 12 bold'),bg="green", fg="white" )
botao_pdv.place(x=950, y=170)

#---------------------------------------------
tela_estoque = Label(frameMeio, text="Estoque",width=90, compound=LEFT,anchor=NW, font=("Verdana", 12, 'bold'), bg='white',fg="#403d3d")
tela_estoque.place(x=950,y=215)

botao_estoque = Button(frameMeio, compound=RIGHT, text="ESTOQUE".upper(),command=add, width=10, font=('Ivy 12 bold'),bg="yellow", fg="black" )
botao_estoque.place(x=950, y=250)


#--------------------------------------------------------------------------------
################# DEFININDO TREE GLOBAL###############
global tree
#inserir categotia
def inserir_categoria_b():
    nome = e_categoria.get()

    lista_inserir = [nome]

    for i in lista_inserir:
        if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return 
#passando a lista para a função inserir
    inserir_categoria(lista_inserir)
    messagebox.showinfo('Sucesso','Os dados foram inseridos com sucesso')

    e_categoria.delete(0, 'end')
    #Pegando os valores da categoria
    categorias_funcao = ver_categoria()
    categorias = []

    for i in categorias_funcao:
        categorias.apendd(i[1])

    #Atualizando a lista de categorias    
    combo_categoria_despesas['values'] = (categorias)  

########inserir Receitas
def inserir_receitas_b():
    nome = 'Receita' 
    data = e_cal_receitas.get()   
    quantia = e_valor_receitas.get()

    lista_inserir = [nome, data, quantia]

    for i in lista_inserir:
        if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return

    inserir_receitas(lista_inserir)
    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

    e_cal_receitas.delete(0, 'end')
    e_valor_receitas.delete(0, 'end')
# atualizando dados
    mostrar_renda()
    percentagem()
    grafico_bar()
    resumo()
    grafico_pie()

#######Inserir despesas
def inserir_despesas_b():
    nome = combo_categoria_despesas.get() 
    data = e_cal_despesas.get()   
    quantia = e_valor_despesas.get()

    lista_inserir = [nome, data, quantia]

    for i in lista_inserir:
        if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return

        inserir_despesas(lista_inserir)
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

        combo_categoria_despesas.delete(0,'end')
        e_cal_despesas.delete(0, 'end')
        e_valor_despesas.delete(0, 'end')

        mostrar_renda()
        percentagem()
        grafico_bar()
        resumo()
        grafico_pie()

# função deletar
def deletar_dados():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]
        nome = treev_lista[1]
        
        if nome =='Receita':
            deletar_receitas([valor])
            messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

            mostrar_renda()
            percentagem()
            grafico_bar()
            resumo()
            grafico_pie()

        else:
            deletar_despesas([valor])
            messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

            mostrar_renda()
            percentagem()
            grafico_bar()
            resumo()
            grafico_pie()

    except IndexError:
             messagebox.showierror('Erro!', 'Selecione os dados na tabela')  
	     


#-------------------------------------------------------------------------------
################# Percentagem progress bar ###############

def percentagem():
    l_nome = Label(frameMeio, text="Porcetagem de Despesas Restante",height=1,anchor=NW, font=("Verdana",16,"bold"),bg='white',fg="#403d3d")
    l_nome.place(x=7,y=5)

    style = ttk.Style()
    style.theme_use('default')
    style.configure("black.Horizontal.TProgressbar", background='#daed6b')
    style.configure("TProgressbar", thickness=25)

    bar = Progressbar(frameMeio, length=180, style='black.Horizontal.TProgressbar')
    bar.place(x=10, y=35)
    
    bar['value'] = 50

    valor = 50

    l_percentagem = Label(frameMeio, text='{:,.2f} %'.format(valor), height=1,anchor=NW, font=('Verdana 12 '), bg="#feffff", fg="#403d3d")
    l_percentagem.place(x=200, y=35)


################# Grafico barra ###############

def grafico_bar():
    # obtendo valores de meses
    lista_categorias = ['Renda','Despesas','Saldo']
    lista_valores = bar_valores()
    
    # faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(4, 3.45), dpi=60)
    ax = figura.add_subplot(111)
    ax.autoscale(enable=True, axis='both', tight=None)
    ax.bar(lista_categorias, lista_valores,  color=colors, width=0.9)

    # create a list to collect the plt.patches data
    c = 0
 
    # set individual bar lables using above list
    for i in ax.patches:
        # get_x pulls left or right; get_height pushes up or down
        ax.text(i.get_x()-.001, i.get_height()+.5,
                str("{:,.0f}".format(lista_valores[c])), fontsize=17, fontstyle='italic',  verticalalignment='bottom',color='dimgrey')

        c += 1

    ax.set_xticklabels(lista_categorias, fontsize=16)
    ax.patch.set_facecolor('#ffffff')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(False)
    ax.xaxis.grid(False)
    canva = FigureCanvasTkAgg(figura, frameMeio)
    canva.get_tk_widget().place(x=10, y=70)



################# funcao de resumo total ###############
def resumo():

    valor = bar_valores()

    l_linha = Label(frameMeio, text="", width=215, height=1,anchor=NW, font=('arial 1 '), bg='#545454',)
    l_linha.place(x=309, y=52)
    l_sumario = Label(frameMeio, text="Total Renda Mensal      ".upper(), height=1,anchor=NW, font=('Verdana 12'), bg=co1, fg='#83a9e6')
    l_sumario.place(x=306, y=35)
    l_sumario = Label(frameMeio, text='R$ {:,.2f}'.format(valor[0]), height=1,anchor=NW, font=('arial 17 '), bg=co1, fg='#545454')
    l_sumario.place(x=306, y=70)

    l_linha = Label(frameMeio, text="", width=215, height=1,anchor=NW, font=('arial 1 '), bg='#545454',)
    l_linha.place(x=309, y=132)
    l_sumario = Label(frameMeio, text="Total Despesas Mensais".upper(), height=1,anchor=NW, font=('Verdana 12'), bg=co1, fg='#83a9e6')
    l_sumario.place(x=306, y=115)
    l_sumario = Label(frameMeio, text='R$ {:,.2f}'.format(valor[1]), height=1,anchor=NW, font=('arial 17 '), bg=co1, fg='#545454')
    l_sumario.place(x=306, y=150)

    l_linha = Label(frameMeio, text="", width=215, height=1,anchor=NW, font=('arial 1 '), bg='#545454',)
    l_linha.place(x=309, y=207)
    l_sumario = Label(frameMeio, text="Total Saldo da Caixa    ".upper(), height=1,anchor=NW, font=('Verdana 12'), bg=co1, fg='#83a9e6')
    l_sumario.place(x=306, y=190)
    l_sumario = Label(frameMeio, text='R$ {:,.2f}'.format(valor[2]), height=1,anchor=NW, font=('arial 17 '), bg=co1, fg='#545454')
    l_sumario.place(x=306, y=220)



################# grafico pie ###############

frame_gra_pie = Frame(frameMeio, width=580, height=250,bg="#4fa882")
frame_gra_pie.place(x=415, y=5)

def grafico_pie():
    # faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(5, 3), dpi=90)
    ax = figura.add_subplot(111)

    lista_valores = pie_valores()[1]
    lista_categorias =  pie_valores()[0]

    # only "explode" the 2nd slice (i.e. 'Hogs')
    explode = []
    for i in lista_categorias:
        explode.append(0.05)
    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors,shadow=True, startangle=90)
    ax.legend(lista_categorias, loc="center right", bbox_to_anchor=(1.55, 0.50))

    canva_categoria = FigureCanvasTkAgg(figura, frame_gra_pie)
    canva_categoria.get_tk_widget().grid(row=0,column=0)



################# criando frames FRAME BAIXO ###############
frame_renda = Frame(frameBaixo, width=300, height=250,bg="#feffff")
frame_renda.grid(row=0,column=0)

frame_operacoes = Frame(frameBaixo, width=220, height=250,bg="#feffff")
frame_operacoes.grid(row=0,column=1, padx=5)

frame_configuracao = Frame(frameBaixo, width=220, height=250,bg="#feffff")
frame_configuracao.grid(row=0,column=2, padx=5)

l_tabela = Label(frameMeio, text="Tabela Receitas e Despesas", height=1, anchor=NW, font=('Verdana 12 bold'), bg="#feffff", fg="#403d3d")
l_tabela.place(x=5, y=309)

#############funcao para mostrar_renda##############
def mostrar_renda():
    # creating a treeview with dual scrollbars
    tabela_head = ['#Id','Categoria','Data','Quantia']

    lista_itens = tabela()

    global tree

    tree = ttk.Treeview(frame_renda, selectmode="extended",columns=tabela_head, show="headings")
    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_renda, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frame_renda, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    hd=["center","center","center", "center"]
    h=[30,100,100,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])

        n+=1

    for item in lista_itens:
        tree.insert('', 'end', values=item)


################# Configuraçõe Despesas  ###############
l_info = Label(frame_operacoes, text="Insira novas despesas", height=1,anchor=NW,relief="flat", font=('Verdana 12 bold'), bg="#feffff", fg="#403d3d")
l_info.place(x=10, y=10)

l_categoria = Label(frame_operacoes, text="Categoria", height=1,anchor=NW,relief="flat", font=('Ivy 12'), bg="#feffff", fg="#403d3d")
l_categoria.place(x=10, y=40)
#---------------------------------------------------------------------
# Pegando os categorias
categorias_funcao = ver_categoria()
categorias = []

for i in categorias_funcao:
    categorias.append(i[1])

combo_categoria_despesas = ttk.Combobox(frame_operacoes, width=10,font=('Ivy 12'))
combo_categoria_despesas['values'] = (categorias)
combo_categoria_despesas.place(x=110, y=41)
#---------------------------------------------------------------------------------
# Entradas de despesas
l_cal_despeas = Label(frame_operacoes, text="Data", height=1,anchor=NW, font=('Ivy 12 '), bg="#feffff", fg="#403d3d")
l_cal_despeas.place(x=10, y=70)

e_cal_despesas = DateEntry(frame_operacoes, width=15, background='darkblue', foreground='sky blue', borderwidth=2, year=2023)
e_cal_despesas.place(x=110, y=71)

#---------------------------------------------------------------------------------
# Entradas de valor despesas
l_valor_despesas = Label(frame_operacoes, text="Quantia Total".upper(), height=1,anchor=NW, font=('Ivy 9 '), bg="#feffff", fg="#403d3d")
l_valor_despesas.place(x=10, y=100)
e_valor_despesas = Entry(frame_operacoes, width=17, justify='left',relief="solid", bg="sky blue", fg="#403d3d")
e_valor_despesas.place(x=110, y=101)
botao_inserir_despesas = Button(frame_operacoes,command=inserir_despesas_b,compound=LEFT, anchor=NW, text=" Despesa".upper(), width=80, overrelief=RIDGE,  font=('Ivy 12 bold'),bg="blue", fg="white" )
botao_inserir_despesas.place(x=110, y=131)

#--------------------------------------------------------------------------------
#  Botão Excluir 
l_excluir = Label(frame_operacoes, text="Excluir ação", height=1,anchor=NW, font=('Ivy 12 bold'), bg="#feffff", fg="#403d3d")
l_excluir.place(x=10, y=190)
botao_deletar = Button(frame_operacoes,command=deletar_dados, compound=LEFT, anchor=NW, text=" Deletar".upper(), width=80, overrelief=RIDGE,  font=('Ivy 12 bold'),bg="red", fg="White" )
botao_deletar.place(x=110, y=190)

#-----------------------------------------------------------------------------------
################ Configuracoes Receitas ###########################

####Receitas
l_descricao = Label(frame_configuracao, text="Insira novas Categoria", height=1,anchor=NW,relief="flat", font=('Verdana 12 bold'), bg="#feffff", fg="#403d3d")
l_descricao.place(x=10, y=130)
'''
l_cal_receitas = Label(frame_configuracao, text="Data", height=1,anchor=NW, font=('Ivy 12 '), bg="#feffff", fg="#403d3d")
l_cal_receitas.place(x=10, y=40)
e_cal_receitas = DateEntry(frame_configuracao, width=17, background='darkblue', foreground='white', borderwidth=2, year=2023)
e_cal_receitas.place(x=110, y=41)

l_valor_receitas = Label(frame_configuracao, text="Quantia Total", height=1,anchor=NW, font=('Ivy 12 '), bg="#feffff", fg="#403d3d")
l_valor_receitas.place(x=10, y=70)
e_valor_receitas = Entry(frame_configuracao, width=17, justify='left',relief="solid",bg="#feffff", fg="#403d3d")
e_valor_receitas.place(x=110, y=71)

#---------------------------------------------------------------------------------
# Botao Inserir receitas
botao_inserir_receitas = Button(frame_configuracao, command=inserir_receitas_b,compound=LEFT, anchor=NW, text=" Adicionar".upper(), width=80, overrelief=RIDGE,  font=('Ivy 12 bold'),bg="green", fg="White")
botao_inserir_receitas.place(x=110, y=111)
'''
#-----------------------------------------------------------------------------------
# operacao Nova Categoria ----------------------
l_info = Label(frame_configuracao, text="Categoria", height=1,anchor=NW, font=('Ivy 12 bold'), bg="#feffff", fg="#403d3d")
l_info.place(x=10, y=160)
e_categoria = Entry(frame_configuracao, width=17, justify='left',relief="solid", bg="sky blue", fg="#403d3d")
e_categoria.place(x=110, y=160)

# Botao Inserir nova categoria
botao_inserir_categoria = Button(frame_configuracao, command=inserir_categoria_b, compound=LEFT, anchor=NW, text=" Adicionar".upper(), width=80, overrelief=RIDGE,  font=('Ivy 12 bold'),bg="green", fg="White" )
botao_inserir_categoria.place(x=110, y=190)


mostrar_renda() 
percentagem()
grafico_bar()
resumo()
grafico_pie()


janela.mainloop ()
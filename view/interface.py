import tkinter as tk
from tkinter import *
import py.funcionario
LARGE_FONT= ("Verdana", 12)

class papaTerra(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)       
        
        self.frames = {}

        for F in (StartPage, telaFuncionario, cadastrarVoo, cadastrarPassageiro, inserirPassageiro, telaCliente):

            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent, bg='#6495ED')

        label = tk.Label(self, text="Bem vindo ao Aeroporto Papa Terra", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Tela funcionario",
                            command=lambda: controller.show_frame(telaFuncionario))
        button.pack()
        button = tk.Button(self, text="Tela cliente",
                            command=lambda: controller.show_frame(telaCliente))
        button.pack()
        button = tk.Button(self, text="Sair",
                            command=lambda: controller.show_frame(telaFuncionario))
        button.pack()



class telaFuncionario(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Tela funcionário", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Voltar",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Cadastrar voo",
                            command=lambda: controller.show_frame(cadastrarVoo))
        button2.pack()
        button3 = tk.Button(self, text="Cadastrar passageiro",
                            command=lambda: controller.show_frame(cadastrarPassageiro))
        button3.pack()

        button4 = tk.Button(self, text="Inserir Passageiro em um Voo",
                            command=lambda: controller.show_frame(inserirPassageiro))
        button4.pack()
        button5 = tk.Button(self, text="Informações sobre Voos",
                            command=lambda: controller.show_frame(cadastrarVoo))
        button5.pack()


class cadastrarVoo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        def add_voo():
            py.funcionario.cadastrarVoo(aerop_text.get(), horas_text.get(), aerod_text.get(), horac_text.get(), quant_text.get())
            limparTexto()
        def limparTexto():
            aerop_entry.delete(0, tk.END)
            horas_entry.delete(0, tk.END)
            aerod_entry.delete(0, tk.END)
            horac_entry.delete(0, tk.END)
            quant_entry.delete(0, tk.END)
        def select_item(event):
            try:
                global item_selecionado
                index = voos_list.curselection()[0]
                item_selecionado = voos_list.get(index)

                aerop_entry.delete(0, tk.END)
                aerop_entry.insert(tk.END, item_selecionado[1])
                horas_entry.delete(0, tk.END)
                horas_entry.insert(tk.END, item_selecionado[2])
                aerod_entry.delete(0, tk.END)
                aerod_entry.insert(tk.END, item_selecionado[3])
                horac_entry.delete(0, tk.END)
                horac_entry.insert(tk.END, item_selecionado[4])
                quant_entry.delete(0, tk.END)
                quant_entry.insert(tk.END, item_selecionado[5])
            except IndexError:
                pass
         #aeroportoPartida
        aerop_text = tk.StringVar()
        aerop_label = tk.Label(self, text="Aeroporto de Partida", font=('bold', 14))
        aerop_label.grid(row=1, column=0, sticky=W)
        aerop_entry = tk.Entry(self, textvariable=aerop_text)
        aerop_entry.grid(row=1, column=1)
         #horarioSaida
        horas_text = tk.StringVar()
        horas_label = tk.Label(self, text="Horário de saída", font=('bold', 14), pady=20)
        horas_label.grid(row=2, column=0, sticky=W)
        horas_entry = tk.Entry(self, textvariable=horas_text)
        horas_entry.grid(row=2, column=1)
         #aeroportoDestino
        aerod_text = tk.StringVar()
        aerod_label = tk.Label(self, text="Aeroporto de destino", font=('bold', 14))
        aerod_label.grid(row=1, column=2, sticky=W)
        aerod_entry = tk.Entry(self, textvariable=aerod_text)
        aerod_entry.grid(row=1, column=3)
         #horarioChegada
        horac_text = tk.StringVar()
        horac_label = tk.Label(self, text="Horário de chegada", font=('bold', 14))
        horac_label.grid(row=2, column=2, sticky=W)
        horac_entry = tk.Entry(self, textvariable=horac_text)
        horac_entry.grid(row=2, column=3)
         #quantidadeAssentos
        quant_text = tk.StringVar()
        quant_label = tk.Label(self, text="Número de assentos", font=('bold', 14))
        quant_label.grid(row=3, column=0)
        quant_entry = tk.Entry(self, textvariable=quant_text)
        quant_entry.grid(row=3, column=1)
        #botões
        inserir_btn = tk.Button(self, text="Adicionar voo", width=12, command=add_voo)
        inserir_btn.grid(row=3, column=2)

        remover_btn = tk.Button(self, text="Remover voo", width=12, command=add_voo)
        remover_btn.grid(row=3, column=3)

        limpar_btn = tk.Button(self, text="Limpar tela", width=12, command=limparTexto)
        limpar_btn.grid(row=4, column=3)

        voltar_btn = tk.Button(self, text="Voltar", command=lambda: controller.show_frame(telaFuncionario))
        voltar_btn.grid(row=0, column=0, sticky=W)
        
        #lista de voos
        voos_list = tk.Listbox(self, height=8, width=75, border=1)
        voos_list.grid(row=4, column=0, columnspan=3, rowspan=6, pady=10)
        #scroll
        scrollbar = tk.Scrollbar(self)
        scrollbar.grid(row=4, column=2, sticky=E)


       
        #set scroll to list
        voos_list.configure(yscrollcommand= scrollbar.set)
        scrollbar.configure(command=voos_list.yview)

        voos_list.bind('<<ListboxSelect>>', select_item)

        def criarLista():
            voos = py.funcionario.listarVoos()
            print(voos)
            for item in voos:
                voos_list.insert(tk.END, item)
        criarLista()

class cadastrarPassageiro(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        def add_passageiro():
            py.funcionario.cadastrarPassageiro(nome_text.get(), cpf_text.get(), telefone_text.get(), email_text.get())
            limparTexto()
        def limparTexto():
            nome_entry.delete(0, tk.END)
            cpf_entry.delete(0, tk.END)
            telefone_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)
        def select_item(event):
            try:
                global item_selecionado
                index = passageiros_list.curselection()[0]
                item_selecionado = passageiros_list.get(index)

                nome_entry.delete(0, tk.END)
                nome_entry.insert(tk.END, item_selecionado[1])
                cpf_entry.delete(0, tk.END)
                cpf_entry.insert(tk.END, item_selecionado[2])
                telefone_entry.delete(0, tk.END)
                telefone_entry.insert(tk.END, item_selecionado[3])
                email_entry.delete(0, tk.END)
                email_entry.insert(tk.END, item_selecionado[4])
            except IndexError:
                pass

        nome_text = tk.StringVar()
        nome_label = tk.Label(self, text="Nome", font=('bold', 14))
        nome_label.grid(row=1, column=0, sticky=W)
        nome_entry = tk.Entry(self, textvariable=nome_text)
        nome_entry.grid(row=1, column=1)

        cpf_text = tk.StringVar()
        cpf_label = tk.Label(self, text="CPF", font=('bold', 14), pady=20)
        cpf_label.grid(row=2, column=0, sticky=W)
        cpf_entry = tk.Entry(self, textvariable=cpf_text)
        cpf_entry.grid(row=2, column=1)

        telefone_text = tk.StringVar()
        telefone_label = tk.Label(self, text="Telefone", font=('bold', 14))
        telefone_label.grid(row=1, column=2, sticky=W)
        telefone_entry = tk.Entry(self, textvariable=telefone_text)
        telefone_entry.grid(row=1, column=3)

        email_text = tk.StringVar()
        email_label = tk.Label(self, text="Email", font=('bold', 14))
        email_label.grid(row=2, column=2, sticky=W)
        email_entry = tk.Entry(self, textvariable=email_text)
        email_entry.grid(row=2, column=3)

        #botões
        inserir_btn = tk.Button(self, text="Adicionar passageiro", width=18, command=add_passageiro)
        inserir_btn.grid(row=3, column=0, padx=10)

        remover_btn = tk.Button(self, text="Remover passageiro", width=18, command=add_passageiro)
        remover_btn.grid(row=3, column=1, padx=10)

        limpar_btn = tk.Button(self, text="Limpar tela", width=12, command=limparTexto)
        limpar_btn.grid(row=3, column=2, sticky=W,padx=10)

        voltar_btn = tk.Button(self, text="Voltar", command=lambda: controller.show_frame(telaFuncionario))
        voltar_btn.grid(row=0, column=0, sticky=W)

        #lista de passageiros
        passageiros_list = tk.Listbox(self, height=8, width=68, border=1)
        passageiros_list.grid(row=4, column=0, columnspan=4, rowspan=6, pady=10)
        #scroll
        scrollbar = tk.Scrollbar(self)
        scrollbar.grid(row=4, column=3, sticky=N, pady=10)
        #set scroll to list
        passageiros_list.configure(yscrollcommand= scrollbar.set)
        scrollbar.configure(command=passageiros_list.yview)

        passageiros_list.bind('<<ListboxSelect>>', select_item)

        def criarLista():
            voos = py.funcionario.listarPassageiros()
            print(voos)
            for item in voos:
                passageiros_list.insert(tk.END, item)
        criarLista()

class inserirPassageiro(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        def inserir_passageiro():
            py.funcionario.inserirPassageiro( codVoo_text.get(), codPassageiro_text.get(), assento_text.get(), classe_text.get())
            limparTexto()
        def limparTexto():
            codPassageiro_entry.delete(0, tk.END)
            codVoo_entry.delete(0, tk.END)
            assento_entry.delete(0, tk.END)

        def select_passageiro(event):
            try:
                global item_selecionado
                index = passageiros_list.curselection()[0]
                item_selecionado = passageiros_list.get(index)

                codPassageiro_entry.delete(0, tk.END)
                codPassageiro_entry.insert(tk.END, item_selecionado[0])
            except IndexError:
                pass
        def select_voo(event):
            try:
                global item_selecionado
                index = voos_list.curselection()[0]
                item_selecionado = voos_list.get(index)

                codVoo_entry.delete(0, tk.END)
                codVoo_entry.insert(tk.END, item_selecionado[0])
            except IndexError:
                pass

        codPassageiro_text = tk.StringVar()
        codPassageiro_label = tk.Label(self, text="Cod passageiro", font=('bold', 14))
        codPassageiro_label.grid(row=1, column=0, sticky=W)
        codPassageiro_entry = tk.Entry(self, textvariable=codPassageiro_text)
        codPassageiro_entry.grid(row=1, column=1)

        codVoo_text = tk.StringVar()
        codVoo_label = tk.Label(self, text="Cod voo", font=('bold', 14))
        codVoo_label.grid(row=1, column=2, sticky=W)
        codVoo_entry = tk.Entry(self, textvariable=codVoo_text)
        codVoo_entry.grid(row=1, column=3)

        classe_text = tk.IntVar()
        classe_label = tk.Label(self, text="Classe", font=('bold', 14))
        classe_label.grid(row=3, column=0, sticky=W)
        tk.Radiobutton(self, text="Econômica", variable=classe_text, value=1).grid(row=2, column=1, sticky=W)
        tk.Radiobutton(self, text="Executiva", variable=classe_text, value=2).grid(row=3, column=1, sticky=W)
        tk.Radiobutton(self, text="Primeira", variable=classe_text, value=3).grid(row=4, column=1, sticky=W)

        assento_text = tk.StringVar()
        assento_label = tk.Label(self, text="Nº do assento", font=('bold', 14))
        assento_label.grid(row=2, column=2, sticky=W)
        assento_entry = tk.Entry(self, textvariable=assento_text)
        assento_entry.grid(row=2, column=3)

        #botões
        inserir_btn = tk.Button(self, text="Inserir passageiro", width=18, command=inserir_passageiro)
        inserir_btn.grid(row=4, column=2, padx=10)

        # remover_btn = tk.Button(self, text="Remover passageiro", width=18, command=inserir_passageiro)
        # remover_btn.grid(row=3, column=3, padx=10)

        limpar_btn = tk.Button(self, text="Limpar tela", width=12, command=limparTexto)
        limpar_btn.grid(row=4, column=3, sticky=W,padx=10)

        voltar_btn = tk.Button(self, text="Voltar", command=lambda: controller.show_frame(telaFuncionario))
        voltar_btn.grid(row=0, column=0, sticky=W)

        passageiros_list_label = tk.Label(self, text="Passageiros:", font=('bold', 14))
        passageiros_list_label.grid(row=5, column=0, pady=10, columnspan=2)
        #lista de passageiros
        passageiros_list = tk.Listbox(self, height=8, width=68, border=1)
        passageiros_list.grid(row=6, column=0, columnspan=4, rowspan=6)
        #scroll
        scrollbar = tk.Scrollbar(self)
        scrollbar.grid(row=6, column=3, sticky=N)
        #set scroll to list
        passageiros_list.configure(yscrollcommand= scrollbar.set)
        scrollbar.configure(command=passageiros_list.yview)
        passageiros_list.bind('<<ListboxSelect>>', select_passageiro)

        voos_list_label = tk.Label(self, text="Voos:", font=('bold', 14))
        voos_list_label.grid(row=13, column=0, columnspan=2, pady=10)
        #lista de voos
        voos_list = tk.Listbox(self, height=8, width=68, border=1)
        voos_list.grid(row=14, column=0, columnspan=4, rowspan=6)
        #scroll
        scrollbar2 = tk.Scrollbar(self)
        scrollbar2.grid(row=14, column=3, sticky=N)
        #set scroll to list
        voos_list.configure(yscrollcommand= scrollbar2.set)
        scrollbar2.configure(command=voos_list.yview)
        voos_list.bind('<<ListboxSelect>>', select_voo)


        def criarListaPassageiros():
            voos = py.funcionario.listarPassageiros()
            print(voos)
            for item in voos:
                passageiros_list.insert(tk.END, item)
        criarListaPassageiros()

        def criarListaVoos():
            voos = py.funcionario.listarVoos()
            print(voos)
            for item in voos:
                voos_list.insert(tk.END, item)
        criarListaVoos()


class telaCliente(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Tela cliente!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(telaFuncionario))
        button2.pack()
        
app = papaTerra()
app.title('Aeroporto Papa Terra')
app.geometry('750x500')
app.mainloop()
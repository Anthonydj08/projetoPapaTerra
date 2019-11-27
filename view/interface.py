import tkinter as tk
from tkinter import *
import py.funcionario
LARGE_FONT= ("Verdana", 12)

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        

        self.frames = {}

        for F in (StartPage, telaFuncionario, cadastrarVoo, telaCliente):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
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
                            command=lambda: controller.show_frame(cadastrarVoo))
        button4.pack()
        button5 = tk.Button(self, text="Informações sobre Voos",
                            command=lambda: controller.show_frame(cadastrarVoo))
        button5.pack()


class cadastrarVoo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        def add_voo():
            py.funcionario.cadastrarVoo2(aerop_text.get(), horas_text.get(), aerod_text.get(), horac_text.get(), quant_text.get())
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
        limpar_btn.grid(row=4, column=3, sticky=W)

        voltar_btn = tk.Button(self, text="Voltar", command=lambda: controller.show_frame(telaFuncionario))
        voltar_btn.grid(row=0, column=0, sticky=W)



        #lista de voos
        voos_list = tk.Listbox(self, height=8, width=50, border=0)
        voos_list.grid(row=4, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
        
        #scroll
        scrollbar = tk.Scrollbar(self)
        scrollbar.grid(row=4, column=2)
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
        


app = SeaofBTCapp()
app.title('Aeroporto Papa Terra')
app.geometry('700x300')
app.mainloop()
import csv
import funcionario
import passageiro


def func():
    sair = False
    while (sair == False):
        op = int(input('Digite:\n1 - Cadastrar Voo \n2 - Cadastrar Passageiro\n3 - Inserir Passageiro em um Voo\n4 - Verificar Lucro\n5 - Informações sobre Voos\n0 - Sair\n'))
        if op == 1:
            funcionario.cadastrarVoo()
        if op == 2:
            funcionario.cadastrarPassageiro()
        if op == 3:
            funcionario.inserirPassageiro()
        if op == 4:
            #funcionario.verificarLucro()
            print("a")
        if op == 5:
            #funcionario.infoVoo()
             print("a")
        elif op == 0:
            sair = True



def cli():
    sair = False
    while (sair == False):
        op = int(
            input('Digite:\n1 - Classe Execultiva\n2 - Classe Econômica\n0 - Sair\n'))
        if op == 1:
            #passageiro.classePremium()
             print("a")
        if op == 2:
            #passageiro.classeEconomica()
             print("a")
        if op == 0:
            sair = True


sair = False
while (sair == False):
    op = int(input('Digite:\n1 - Funcionario\n2 - Cliente\n0 - Sair\n'))
    if op == 1:
        func()
    elif op == 2:
        cli()
    elif op == 0:
        sair = True

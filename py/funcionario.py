import csv
from pandas import DataFrame

def inserirPassageiro():

  tabela = []
  with open("csv/voo.csv") as csvfile:
      arq = csv.reader(csvfile)
      for row in arq:
          tabela.append(row)
          voos = DataFrame(tabela, columns = ['cod', 'aeroPartida', 'aeroDestino', 'tempoEstimado', 'quantidadeAssentos'])

  tabela2 = []
  with open('csv/passageiro.csv') as csvfile:
      voo = csv.reader(csvfile)
      for row in voo:
          tabela2.append(row)
          passageiros = DataFrame(tabela2, columns=['cod', 'nome', 'cpf', 'telefone', 'email','valorgasto'])

  print(voos)
  codVoo = input('Código do Voo ')

  print(passageiros)
  codPassageiro = input('Código do Passageiro ')
  numeroAssento = input('Numero do assento ')
  classePassageiro = input('Classe do passageiro ')

  with open('voos/'+codVoo+'.csv', 'a') as voo:
      writer = csv.writer(voo)
      writer.writerow([codVoo, codPassageiro, classePassageiro, numeroAssento])
      voo.close()
 

def cadastrarVoo():
  codVoo = input('Código do Voo ')
  aeroPartida = input('Aeroporto de partida ')
  aeroDestino = input('Aeroporto de destino ')
  tempoEstimado = input('Tempo estimado ')
  quantidadeAssentos = input('Quantidade de assentos ')

  with open('csv/voo.csv', 'a') as voo:
      writer = csv.writer(voo)
      writer.writerow([codVoo, aeroPartida, aeroDestino, tempoEstimado, quantidadeAssentos])
      voo.close()
      
  f = open('voos/'+codVoo+'.csv', 'a')

def cadastrarPassageiro():
  codPassageiro = input('Codigo do passageiro ')
  nome = input('Nome do passageiro ')
  cpf = input('CPF do passageiro ')
  Telefone = int(input('Telefone do passageiro '))
  email = input('Email do passageiro ')
  valorGasto = 0
  
  with open('csv/passageiro.csv', 'a') as passageiro:
    writer = csv.writer(passageiro)
    writer.writerow([codPassageiro, nome, cpf, Telefone, email, valorGasto])
    passageiro.close()

def func():
  sair = False
  while (sair == False):
    op = int(input('Digite:\n1 - Cadastrar Voo \n2 - Cadastrar Passageiro\n3 - Inserir Passageiro em um Voo\n4 - Verificar Lucro\n5 - Informações sobre Voos\n0 - Sair\n'))
    if op == 1:
      cadastrarVoo()
    if op == 2:
      cadastrarPassageiro()
    if op == 3:
      inserirPassageiro()
    # if op == 4:
    #   verificarLucro()
    # if op == 5:
    #   infoVoo()
    elif op == 0:
      sair = True
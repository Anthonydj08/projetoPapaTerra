import csv
from pandas import DataFrame
import numpy as np

def inserirPassageiro():

  tabela = []
  with open("voo.csv") as csvfile:
      arq = csv.reader(csvfile)
      for row in arq:
          tabela.append(row)
          voos = DataFrame(tabela, columns = ['cod', 'aeroPartida', 'aeroDestino', 'tempoEstimado', 'quantidadeAssentos'])

  tabela2 = []
  with open('passageiro.csv') as csvfile:
      voo = csv.reader(csvfile)
      for row in voo:
          tabela2.append(row)
          passageiros = DataFrame(tabela2, columns=['cod', 'nome', 'cpf', 'telefone', 'email','valorgasto'])

  print(voos)
  codVoo = input('Código do Voo ')

  print(passageiros)
  codPassageiro = input('Código do Passageiro ')
  numeroAssento = input('numero do assento ')
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

  with open('voo.csv', 'a') as voo:
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
  
  with open('passageiro.csv', 'a') as passageiro:
    writer = csv.writer(passageiro)
    writer.writerow([codPassageiro, nome, cpf, Telefone, email, valorGasto])
    passageiro.close()


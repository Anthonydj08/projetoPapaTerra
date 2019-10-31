import csv

def economica():
  sair = False
  while (sair == False):
    op = int(input('Digite:\n1 - Coca-Cola R$4,00\n2 - Café R$2,00\n3 - Água R$3,00\n4 - Amendoim R$3,50\n5 - Batatinha Chips R$4,50\n6 - Goiabinha R$4,00\n7 - Bolinho com gostas de Chocolate R$5,00\n0 - Sair\n'))
    if op == 1:
      print()
    elif op == 2:
      print()
    elif op == 3:
      print()
    elif op == 4:
      print()
    elif op == 5:
      print()
    elif op == 6:
      print()
    elif op == 7:
      print()
    elif op == 0:
      sair = True

def execultiva():
  sair = False
  while (sair == False):
    op = int(input('Digite:\n1 - whisky R$12,00\n2 - champagne R$10,00\n0 - Sair\n'))
    if op == 1:
      print()
    elif op == 2:
      print()
    elif op == 3:
      print()
    elif op == 4:
      print()
    elif op == 5:
      print()
    elif op == 6:
      print()
    elif op == 7:
      print()
    elif op == 0:
      sair = True

def cli():
  sair = False
  while (sair == False):
    op = int(input('Cardápio:\n1 - Classe Execultiva\n2 - Classe Econômica\n0 - Sair\n'))
    if op == 1:
      execultiva()
    if op == 2:
      economica()
    if op == 0:
      sair = True
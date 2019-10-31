import py.funcionario
import py.passageiro

def menu():
  sair = False
  while (sair == False):
    op = int(input('Digite:\n1 - Funcionario\n2 - Passageiro\n0 - Sair\n'))
    if op == 1:
      py.funcionario.func()
    elif op == 2:
      py.passageiro.cli()
    elif op == 0:
      sair = True
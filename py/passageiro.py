
# Manual de voo
def guiaPassageiro():
  sair = False
  while (sair == False):
    op = int(input("Guia por capítulos:\n1 - Bagagem\n2 - Segurança de voo\n3 - Desembarque\n0 - Sair\n"))
    if op == 1:
      print('Bagagem\n'
            'Qual o tamanho da bagagem de mão permitido?\n'
            '\nOs limites da bagagem de mão são definidos por critérios de\n'
            'segurança para atender ao peso máximo de decolagem do avião e\n'''
            'às ações preventivas de segurança a bordo.\n'
            'Em voos domésticos, a bagagem não pode ser maior do que 115cm\n'
            '(considerando altura + comprimento + largura) e o peso máximo é de 5kg.\n'
            'Caso exceda essa especificação, a companhia aérea poderá exigir que a\n'
            'bagagem não viaje com você e seja despachada.\n')
    elif op == 2:
      print('Segurança de voo\n'
            '\nPor que um avião arremete? isso é perigoso?\n'
            'A arremetida é um procedimento previsto e seguro que não oferece riscos\n'
            'para a aeronave ou para os passageiros.\n'
            'Um piloto decide arremeter quando identifica que as condições para o pouso\n'
            'não estão plenamente favoráveis e planeja fazer uma nova aproximação.\n')

    elif op == 3:
      print('Devolução de bagagem\n'
            '\nQuem é responsável pela devolução da minha bagagem?\n'
            'A companhia área deve devolver a bagagem ao passageiro nas mesmas condições nas quais foi despachada.\n'
            'Ao administrador aeroportuário cabe manter as esteiras e os equipamentos em funcionamento.\n')


    elif op == 0:
      sair = True


import py.funcionario

def economica():
  sair = False
  while (sair == False):
    op = int(input('Digite:\n1 - Coca-Cola R$4,00\n2 - Café R$2,00\n3 - Água R$3,00\n4 - Amendoim R$3,50\n5 - Batatinha Chips R$4,50\n6 - Goiabinha R$4,00\n7 - Bolinho com gostas de Chocolate R$5,00\n0 - Sair\n'))
    if op == 1:
      py.funcionario.inserir_despesas(4)
    elif op == 2:
      py.funcionario.inserir_despesas(2)
    elif op == 3:
      py.funcionario.inserir_despesas(13)
    elif op == 4:
      py.funcionario.inserir_despesas(3.50)
    elif op == 5:
      py.funcionario.inserir_despesas(4.50)
    elif op == 6:
      py.funcionario.inserir_despesas(4)
    elif op == 7:
      py.funcionario.inserir_despesas(5)
    elif op == 0:
      sair = True

def execultiva():
  sair = False
  while (sair == False):
    op = int(input('Digite:\n1 - whisky R$12,00\n2 - champagne R$10,00\n0 - Sair\n'))
    if op == 1:
      py.funcionario.inserir_despesas(12)
    elif op == 2:
      py.funcionario.inserir_despesas(10)
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
    if op == 3:
      guiaPassageiro()
    if op == 0:
      sair = True
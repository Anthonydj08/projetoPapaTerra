from openpyxl import Workbook
from openpyxl import load_workbook

def cadastrarVoo():
  wb = load_workbook('BD.xlsx')
  sheet = wb["Voos"]

  codVoo = sheet.max_row
  aeroPartida = input('Aeroporto de partida ')
  aeroDestino = input('Aeroporto de destino ')
  tempoEstimado = input('Tempo estimado ')
  quantidadeAssentos = input('Quantidade de assentos ')
  
  sheet.append((codVoo, aeroPartida, aeroDestino, tempoEstimado,quantidadeAssentos))
  
  wb.create_sheet('Voo'+str(codVoo))
  BD = wb.get_sheet_by_name('Voo'+str(codVoo))
  BD['A1'] = 'codVoo'
  BD['B1'] = 'codPassageiro'
  BD['C1'] = 'numeroAssento'
  BD['D1'] = 'classePassageiro'
  BD['E1'] = 'valorGasto'

  wb.save("BD.xlsx")

def cadastrarPassageiro():
  wb = load_workbook('BD.xlsx')
  sheet = wb["Passageiros"]

  codPassageiro = sheet.max_row
  nome = input('Nome do passageiro ')
  cpf = input('CPF do passageiro ')
  telefone = input('Telefone do passageiro ')
  email = input('Email do passageiro ')
    
  sheet.append((codPassageiro, nome, cpf, telefone, email))

  wb.save("BD.xlsx")

def criartabela():
  arquivo_excel = Workbook()
  planilha1 = arquivo_excel.active
  planilha1.title = "Voos"
  planilha1 = arquivo_excel.create_sheet("Passageiros")
  
  planilha1 = arquivo_excel.get_sheet_by_name("Voos")

  planilha1["A1"] = "codVoo"
  planilha1["B1"] = "aeroportoPartida"
  planilha1["C1"] = "aeroportoDestino"
  planilha1["D1"] = "tempoEstimado"
  planilha1["E1"] = "quantidadeAssentos"

  planilha1 = arquivo_excel.get_sheet_by_name("Passageiros")

  planilha1["A1"] = "codPassageiro"
  planilha1["B1"] = "nome"
  planilha1["C1"] = "cpf"
  planilha1["D1"] = "telefone"
  planilha1["E1"] = "email"
  
  arquivo_excel.save("BD.xlsx")

# criartabela()


def inserirPassageiro():
  wb = load_workbook('BD.xlsx')

  sheet = wb["Voos"]
  max_linha = sheet.max_row
  max_coluna = sheet.max_column
  for i in range(1, max_linha + 1):
    for j in range(1, max_coluna + 1):
      print(sheet.cell(row=i, column=j).value, end="-")
    print("\n")
    
  codVoo = input('Código do Voo ')

  sheet = wb["Passageiros"]
  max_linha = sheet.max_row
  max_coluna = sheet.max_column
  for i in range(1, max_linha + 1):
    for j in range(1, max_coluna + 1):
      print(sheet.cell(row=i, column=j).value, end="-")
    print("\n")

  codPassageiro = input('Código do Passageiro ')
  numeroAssento = input('Numero do assento ')
  classePassageiro = input('Classe do passageiro ')

  sheet = wb['Voo'+str(codVoo)]
  sheet.append((codVoo, codPassageiro, numeroAssento, classePassageiro))

  wb.save("BD.xlsx")

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
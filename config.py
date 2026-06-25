import os
from datetime import date
def ler_arquivo(arquivo):
      arquivo = open(arquivo,'r')
      usuarios = eval(arquivo.read())
      arquivo.close()
      return usuarios

def escrever_arquivo(arquivo,usuarios):
      arquivo = open(arquivo,'w')
      arquivo.write(str(usuarios))
      arquivo.close()

def definir_status(posicao):
      if posicao:
            s = 'Ativo'
      else:
            s = 'Inativo'
      return s

def formatar_cpf(cpf):
      cpf = cpf.replace('.', '')
      cpf = cpf.replace('-', '')
      cpf = cpf.replace(' ', '')
      return cpf
def validar_cpf(cpf):
      
      tam = len(cpf)
      soma = 0
      d1 = 0
      d2 = 0
      if tam != 11:
            return False
      for i in range(11):
            if (cpf[i]<'0')or(cpf[i]>'9'):
                  return False
      for i in range(9):
            soma += (int(cpf[i])*(10 - i))
      d1 = 11 - (soma % 11)
      if (d1 == 10 or d1 == 11):
            d1 = 0
      if d1 != int(cpf[9]):
            return False
      soma = 0
      for i in range(10):
            soma += (int(cpf[i])*(11-i))
      d2 = 11 - (soma%11)
      if (d2 == 10 or d2 == 11):
            d2 = 0
      if d2 != int(cpf[10]):
            return False
      return True

def validar_email(email):
      valido = False
      while valido==False:
            if '@' in email:
                  valido = True
            else:
                  print("\nFalha. Digite um email válido.")
                  email = input('Digite um email do usuário: ')
      return email

def validar_data(data):
      valido = False
      try:
            data =data.split('-')
            dia = int(data[0])
            mes = int(data[1])
            ano = int(data[2])
            data_hj = date.today()
            if (dia>0 and dia<32) and (mes>0 and mes<13):
                  if ano<data_hj.year:
                        pass
                  elif ano==data_hj.year:
                        if mes == data_hj.month:
                              if dia < data_hj.day:
                                    pass
                              else:
                                    valido = True 
                        elif mes>data_hj.month:
                              valido = True
                  else:
                        valido = True   
                              
            else:
                  pass
      except:
            pass
      return valido
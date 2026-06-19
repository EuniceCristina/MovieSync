import os
def ler_arquivo(arquivo):
      arquivo = open(arquivo,'r')
      usuarios = eval(arquivo.read())
      arquivo.close()
      return usuarios

def escrever_arquivo(arquivo,usuarios):
      arquivo = open(arquivo,'w')
      arquivo.write(str(usuarios))
      arquivo.close()
      
def validar_cpf(cpf):
      cpf = cpf.replace('.', '')
      cpf = cpf.replace('-', '')
      cpf = cpf.replace(' ', '')
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
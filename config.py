def ler_arquivo(arquivo):
      arquivo = open(arquivo,'r')
      usuarios = eval(arquivo.read())
      arquivo.close()
      return usuarios

def escrever_arquivo(arquivo,usuarios):
      arquivo = open(arquivo,'w')
      arquivo.write(str(usuarios))
      arquivo.close()
      
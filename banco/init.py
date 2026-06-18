from datetime import date
data = str(date.today())

def escrever_arquivo(arquivo,usuarios):
      arquivo = open(arquivo,'w')
      arquivo.write(str(usuarios))
      arquivo.close()


lista_usuarios = {
      '1' : ['Eunice','eunice@gmail.com','123',data] 
}



lista_filmes = {
      1 : ['Malevola', 'drama' , 'True']
}

lista_salas = {
      1 : [12,'2D']
}
lista_ingressos = { 
    1 : ['1',1,'meia',data]
    }

lista_sessoes = {
      1: [1, 1, 12, '12-12-2012', 12.0,13.0,12.0,data]
}
escrever_arquivo('banco/usuarios.txt',lista_usuarios)
escrever_arquivo('banco/filmes.txt',lista_filmes)
escrever_arquivo('banco/salas.txt',lista_salas)
escrever_arquivo('banco/ingressos.txt',lista_ingressos)
escrever_arquivo('banco/sessoes.txt', lista_sessoes)


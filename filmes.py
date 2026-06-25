import os
from datetime import date
from banco import *

data = str(date.today())
from config import ler_arquivo,escrever_arquivo,definir_status

def filmes():
      filmes = ler_arquivo('banco/filmes.txt')
      while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("_"*60)
            print(
                  """
Módulo de Filmes 🎞️
                  """)
            print("_"*60)
            
            print("""
╔══════════════════════════════════════════════════════════╗
║                       MENU                               ║
╠══════════════════════════════════════════════════════════╣
║ 0 - Cadastrar Filmes                                     ║
║ 1 - Listar Filmes em Cartaz                              ║
║ 2 - Cancelar Filme                                        ║
║ 3 - Editar Filme                                         ║                                      
║ 4 - Voltar                                               ║
╚══════════════════════════════════════════════════════════╝
      """)
            opcao = int(input('Digite sua ação: '))
            if opcao == 0:
                  os.system('cls' if os.name == 'nt' else 'clear')
                  print("_"*60)
                  print(
                  """
Cadastro de Filmes 🎞️
                  """)
                  print("_"*60)
                  nome = input('\nDigite o nome do seu filme: ')
                  filmes = ler_arquivo('banco/filmes.txt')
                  cod = len(filmes.keys()) + 1
                  generos =['Drama','Terror','Comédia','Ação']
                  print("""
                        \nEscolha o genêro do seu filme 
                        
0 - Drama
1 - Terror
2 - Comédia
3 - Ação
                        \n
                        
                        """)
                  opc = int(input('Sua opção: '))
                  genero = generos[opc]
                  status = True
                  filme = [nome,genero,status]
                  filmes[cod]=filme
                  escrever_arquivo('banco/filmes.txt',filmes)
                        
                  print('\nFilme cadastrado com sucesso!\n')
                  input("Tecle <ENTER> para continuar...")
                  
            elif opcao == 1 :
                  os.system('cls' if os.name == 'nt' else 'clear')
                  print("_"*60)
                  print(
                  """
Lista de Filmes 🎞️
                  """)
                  print("_"*60)
                  print()
                  filmes = ler_arquivo('banco/filmes.txt')
                  for filme in filmes:
                        status = definir_status(filmes[filme][2])
                              
                        print(f'''

Código          : {filme}         
Nome            : {filmes[filme][0]}
Gênero          : {filmes[filme][1]}
Status          : {status}
                              ''')
                        print("_"*60)
            
                        
                  
                        
                  input("Tecle <ENTER> para continuar...")
                  
            elif opcao == 2:
                  os.system('cls' if os.name == 'nt' else 'clear')
                  print("_"*60)
                  print(
                  """
Cancelamento de Filmes 🎞️
                  """)
                  print("_"*60)
                  cod = int(input('\nDigite código do filme que deseja excluir: '))
                  filmes = ler_arquivo('banco/filmes.txt')
                  sessoes = ler_arquivo('banco/sessoes.txt')
                  if filmes[cod]:
                        filmes[cod][2] = False
                        escrever_arquivo('banco/filmes.txt',filmes)
                        print('\nFilme cancelado!\n')
                  
                  else:
                        print('\nFilme não encontrado!')
                  input("Tecle <ENTER> para continuar...")
           
            elif opcao == 3:
                  os.system('cls' if os.name == 'nt' else 'clear')
                  print("_"*60)
                  print(
                  """
Edicão de Filmes 🎞️
                  """)
                  print("_"*60)
                  cod = int(input('\nDigite o codígo do filme que deseja editar: '))
                  filmes = ler_arquivo('banco/filmes.txt')
                  if cod in filmes:
                        nome = input('Digite o nome do filme: ')
                        generos =['Drama','Terror','Comédia','Ação']
                        print("""
                              \nEscolha o genêro do seu filme 
                              
0 - Drama
1 - Terror
2 - Comédia
3 - Ação
                              \n
                              
                              """)
                        opc = int(input('Sua opção: '))
                        genero = generos[opc]
                        status = filmes[cod][2]
                        nov_filme = [nome,genero,status]
                        filmes[cod] = nov_filme
                        escrever_arquivo('banco/filmes.txt',filmes)
                        print('\nFilme editado com sucesso!\n')
                              
                              
                              
                  else:
                        print('\nFilme não encontrado!')
                        input("Tecle <ENTER> para continuar...")
            elif opcao == 4:
                  break
            else:
                  print('\nOpção inválida. Tente novamente.\n')
                  input("Tecle <ENTER> para continuar...")
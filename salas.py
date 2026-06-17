import os
from datetime import date
from banco import *

data = str(date.today())
from config import ler_arquivo,escrever_arquivo

def salas():
      while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("_"*60)
            print(
                  """
            Módulo de Salas 🎞️
                  """)
            print("_"*60)
            
            print("""
      ╔══════════════════════════════════════════════════════════╗
      ║                       MENU                               ║
      ╠══════════════════════════════════════════════════════════╣
      ║ 0 - Cadastrar Salas                                      ║
      ║ 1 - Listar Salas                                         ║
      ║ 2 - Excluir Sala                                        ║
      ║ 3 - Editar Sala                                         ║                                      
      ║ 4 - Voltar                                               ║
      ╚══════════════════════════════════════════════════════════╝
      """)
            opcao = int(input('Digite sua ação: '))
            if opcao == 0:
                  salas = ler_arquivo('banco/salas.txt')
                  os.system('cls' if os.name == 'nt' else 'clear')
                  print("_"*60)
                  print(
                  """
Cadastro de Salas 🎞️
                  """)
                  print("_"*60)
                  salas = ler_arquivo('banco/salas.txt')
                  cod = len(salas.keys()) + 1
                  capacidade = int(input('\nDigite a capacidade da sua sala:'))
                  tipos =['2D','3D','IMAX','VIP']
                  print("""
                        \nEscolha o tipo da sua sala
                        
0 - 2d
1 - 3D
2 - IMAX
3 - VIP
                        \n
                        
                        """)
                  opc = int(input('Sua opção: '))
                  tipo = tipos[opc]
                  dis = True
                  sala = [capacidade,tipo,dis]
                  salas[cod]=sala
                  escrever_arquivo('banco/salas.txt',salas)
                        
                  print('\nSala cadastrada com sucesso!\n')
                  input("Tecle <ENTER> para continuar...")
                  
            elif opcao == 1 :
                  os.system('cls' if os.name == 'nt' else 'clear')
                  print("_"*60)
                  print(
                  """
Lista de Salas 🎞️
                  """)
                  print("_"*60)
                  salas = ler_arquivo('banco/salas.txt')
                  for sala in salas:
                        dis = salas[sala][2]
                        if dis:
                              t = "Disponível"
                        else:
                              t = "Indisponível"
                              
                        print(f'''
            
Código          : {sala}
Capacidade      : {salas[sala][0]}
Tipo            : {salas[sala][1]}
Disponibilidade : {t}
                              ''')
                        print("_"*60)            
                        
                        
                  
                        
                  input("\nTecle <ENTER> para continuar...")
                  
            elif opcao == 2:
                  os.system('cls' if os.name == 'nt' else 'clear')
                  print("_"*60)
                  print(
                  """
Exclusão de Salas 🎞️
                  """)
                  print("_"*60)
                  cod = int(input('\nDigite código do sala que deseja excluir: '))
                  salas = ler_arquivo('banco/salas.txt')
                  sessoes = ler_arquivo('banco/sessoes.txt')
                  exist = False
                  try :
                        if salas[cod]:
                              for sessao in sessoes:
                                    if sessoes[sessao][1]==cod:
                                          exist = True
                              if exist:
                                    print('Sala possui sessões cadastradas.')
                              else:
                                    salas.pop(cod)
                                    escrever_arquivo('banco/salas.txt',salas)
                                    print('\nSala excluída!\n')
                  
                  except:
                        print('\nSala não encontrada!')
                  input("\nTecle <ENTER> para continuar...")
           
            elif opcao == 3:
                  os.system('cls' if os.name == 'nt' else 'clear')
                  print("_"*60)
                  print(
                  """
Edição de Salas 🎞️
                  """)
                  print("_"*60)
                  cod = int(input('\nDigite o codígo do sala que deseja editar: '))
                  salas = ler_arquivo('banco/salas.txt')
                  try:
                        if salas[cod]:
                              capacidade = int(input('Digite a capacidade da sala: '))
                              tipos =['2D','3D','IMAX','VIP']
                              print("""
                                    \nEscolha o tipo da sua sala
                                    
            0 - 2d
            1 - 3D
            2 - IMAX
            3 - VIP
                                    
                                    
                                    """)
                              opc = int(input('Sua opção: '))
                              tipo = tipos[opc]
                              if salas[cod][2]:
                                    status = 'disponivel'
                              else:
                                    status = 'não disponivel'
                              dis = input(f'Sua sala está {status}. Deseja trocar? [S/N] :').upper()
                              if dis=='S':
                                    dis = not salas[cod][2]
                              else:
                                    dis =  salas[cod][2]
                              nov_sala = [capacidade,tipo,dis]
                              salas[cod] = nov_sala
                              escrever_arquivo('banco/salas.txt',salas)
                              print('\nSala editada com sucesso!\n')
                              
                              
                              
                              
                  except:
                        print('\nSala não encontrada!')
                  input("\nTecle <ENTER> para continuar...")
            elif opcao == 4:
                  break
            else:
                  print('\nOpção inválida. Tente novamente.\n')
                  input("\nTecle <ENTER> para continuar...")
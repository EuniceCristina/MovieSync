import os
from datetime import date
from banco import *

data = str(date.today())
from config import ler_arquivo,escrever_arquivo,definir_status


def ingressos():
      while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("_"*60)
            print(
                  """
Módulo de Ingressos 🎟️
                  """)
            print("_"*60)
            print("""
╔══════════════════════════════════════════════════════════╗
║                       MENU                               ║   
║ 0 - Cadastrar Ingressos                                  ║
║ 1 - Listar Ingressos                                     ║
║ 2 - Cancelar Ingresso                                    ║
║ 3 - Editar Ingresso                                      ║                                      
║ 4 - Voltar                                               ║
╚══════════════════════════════════════════════════════════╝
      """)
            
            opcao = int(input('Digite sua ação: '))
            
            if opcao == 0:
                  os.system('cls' if os.name == 'nt' else 'clear')
                  print("_"*60)
                  print(
                        """
Cadastro de Ingressos 🎟️
                        """)
                  print("_"*60)
                  
                  ingressos = ler_arquivo('banco/ingressos.txt')
                  cod = len(ingressos.keys())+1
                  cpf = input('\nDigite cpf do usuário: ')
                  ingressos = ler_arquivo('banco/ingressos.txt')
                  usuarios = ler_arquivo('banco/usuarios.txt')
                  if cpf in usuarios and usuarios[cpf][3]:
                        print('\nSessões disponíveis\n')
                        sessoes = ler_arquivo('banco/sessoes.txt')
                        filmes = ler_arquivo('banco/filmes.txt')
                        exist_s = False
                        for sessao in sessoes:
                             if sessoes[sessao][7]:
                                   exist_s = True
                                   print(f'Código : {sessao}   | Filme : {filmes[sessoes[sessao][0]][0]} |  Vagas : {sessoes[sessao][2]}')
                        if not exist_s:
                              print('\nSem sesões atividas. Cadastre uma sessão')
                        else:
                              sessao = int(input('Digite o código da sessão que deseja comprar ingresso: ')) 
                              if sessao in sessoes and sessoes[sessao][7]:
                                    if sessoes[sessao][2]>0:
                                          
                                          valor = float(input('Digite o valor do ingresso: '))
                                          tipo = input('Digite o tipo do ingresso: ')
                                          status = True 
                                          data_hj = str(date.today())
                                          ingresso = [cpf,sessao,tipo,valor,status,data_hj]
                                          ingressos[cod]=ingresso
                                          sessoes[sessao][2] = sessoes[sessao][2] -1
                                          escrever_arquivo('banco/sessoes.txt',sessoes)
                                          escrever_arquivo('banco/ingressos.txt',ingressos)
                                                
                                          print('\nIngresso cadastrado com sucesso!\n')
                                    else:
                                          print('Não existem mais vagas para essa sessão. Tente novamente.')
                              else:
                                    print("Sessão não cadastrada ou indisponicel. Tente novamente")
                        
                  else:
                        print("Usuário não cadastrado ou indisponivel!Tente novamente")
                        
                  
                  input("Tecle <ENTER> para continuar...")
                        
            elif opcao == 1 :
                  os.system('cls' if os.name == 'nt' else 'clear')
                  print("_"*60)
                  print(
                        """
Lista de Ingressos 🎟️
                        """)
                  print("_"*60)
                  print()
                  ingressos = ler_arquivo('banco/ingressos.txt')
                  usuarios = ler_arquivo('banco/usuarios.txt')
                  filmes = ler_arquivo('banco/filmes.txt')
                  for ingresso in ingressos:
                        status = definir_status(ingressos[ingresso][4])
                        print(f'''

Código  : {ingresso}
Usuário : {usuarios[ingressos[ingresso][0]][0]}
Sessão  : {ingressos[ingresso][1] }
Valor   : {ingressos[ingresso][3]}
Tipo    : {ingressos[ingresso][2]}
Status  : {status}

                                               ''')
                        print("_"*60)
                  input("\nTecle <ENTER> para continuar...")
                              
                        
                              
                        
                        
            elif opcao == 2:
                  os.system('cls' if os.name == 'nt' else 'clear')
                  print("_"*60)
                  print(
                        """
Cancelamento de Ingressos 🎟️
                        """)
                  print("_"*60)
                  cod = int(input('\nDigite código do ingresso que deseja cancelar: '))
                  ingressos = ler_arquivo('banco/ingressos.txt')
                  sessoes = ler_arquivo('banco/sessoes.txt')
                  if cod in ingressos:
                        sessoes[ingressos[cod][1]][2]= sessoes[ingressos[cod][1]][2]+1
                        ingressos[ingresso][4]=False
                        escrever_arquivo("banco/sessoes.txt",sessoes)
                        escrever_arquivo('banco/ingressos.txt',ingressos)
                        print('\nIngresso cancelado!\n')
                              
                  else:
                        print('\nIngresso não encontrado!')
                  input("Tecle <ENTER> para continuar...")
                        
            elif opcao == 3:
                  os.system('cls' if os.name == 'nt' else 'clear')
                  print("_"*60)
                  print(
                        """
Edição de Ingressos 🎟️
                        """)
                  print("_"*60)
                  cod = int(input('\nDigite o codígo do ingresso que deseja editar: '))
                  ingressos = ler_arquivo('banco/ingressos.txt')
                  if cod in ingressos:
                        cpf = input('\nDigite cpf do usuário: ')
                        usuarios = ler_arquivo('banco/usuarios.txt')
                        if cpf in usuarios and usuarios[cpf][3]:
                              print('\nSessões disponíveis\n')
                              sessoes = ler_arquivo('banco/sessoes.txt')
                              filmes = ler_arquivo('banco/filmes.txt')
                              exist_s = False
                              for sessao in sessoes:
                                    if sessoes[sessao][7]:
                                          exist_s = True
                                          print(f'Código : {sessao}   | Filme : {filmes[sessoes[sessao][0]][0]} |  Vagas : {sessoes[sessao][2]}')
                              if not exist_s:
                                    print('\nSem sesões atividas. Cadastre uma sessão')
                              else:
                                    sessao = int(input('Digite o código da sessão que deseja comprar ingresso: ')) 
                                    if sessao in sessoes and sessoes[sessao][7]:
                                          if sessoes[sessao][2]>0:
                                                
                                                valor = float(input('Digite o valor do ingresso: '))
                                                tipo = input('Digite o tipo do ingresso: ')
                                                status = True 
                                                data_hj = str(date.today())
                                                ingresso = [cpf,sessao,tipo,valor,status,data_hj]
                                                sessoes[ingressos[cod][1]][2] = sessoes[ingressos[cod][1]][2] + 1
                                                ingressos[cod]=ingresso
                                                sessoes[sessao][2] = sessoes[sessao][2] -1
                                                escrever_arquivo('banco/sessoes.txt',sessoes)
                                                escrever_arquivo('banco/ingressos.txt',ingressos)
                                                      
                                                print('\nIngresso cadastrado com sucesso!\n')
                                          else:
                                                print('Não existem mais vagas para essa sessão. Tente novamente.')
                                    else:
                                          print("Sessão não cadastrada ou indisponivel. Tente novamente")
                              
                        else:
                              print("Usuário não cadastrado ou indisponivel!Tente novamente")
                  else:
                        print('Ingresso não encontrado. Tente novamente')
                  input("Tecle <ENTER> para continuar...")
            elif opcao == 4:
                  break
            else:
                  print('\nOpção inválida. Tente novamente.\n')
                  input("Tecle <ENTER> para continuar...")

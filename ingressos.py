import os
from datetime import date
from banco import *

data = str(date.today())
from config import ler_arquivo,escrever_arquivo


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
      ╠══════════════════════════════════════════════════════════╣
      ║ 0 - Cadastrar Ingressos                                  ║
      ║ 1 - Listar Ingressos Disponíveis                         ║
      ║ 2 - Excluir Ingresso                                     ║
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
                  if cpf in usuarios:
                        print('\nSessões disponíveis\n')
                        sessoes = ler_arquivo('banco/sessoes.txt')
                        filmes = ler_arquivo('banco/filmes.txt')
                        for sessao in sessoes:
                             print(f'Código : {sessao}   | Filme : {filmes[sessoes[sessao][0]][0]} |  Vagas : {sessoes[sessao][2]}')
                        sessao = int(input('Digite o código da sessão que deseja comprar ingresso: ')) 
                        if sessao in sessoes:
                              if sessoes[sessao][2]>0:
                                    
                                    valor = float(input('Digite o valor do ingresso: '))
                                    tipo = input('Digite o tipo do ingresso: ')
                                    data_hj = str(date.today())
                                    ingresso = [cpf,sessao,valor,tipo,data_hj]
                                    ingressos[cod]=ingresso
                                    sessoes[sessao][2] = sessoes[sessao][2] -1
                                    escrever_arquivo('banco/sessoes.txt',sessoes)
                                    escrever_arquivo('banco/ingressos.txt',ingressos)
                                          
                                    print('\nIngresso cadastrado com sucesso!\n')
                              else:
                                    print('Não existem mais vagas para essa sessão. Tente novamente.')
                        else:
                              print("Sessão não cadastrada. Tente novamente")
                  else:
                        print("Usuário não cadastrado!Tente novamente")
                        
                  
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
                        print(f'''

Código  : {ingresso}
Usuário : {usuarios[ingressos[ingresso][0]][0]}
Sessão  : {ingressos[ingresso][1] }
Valor   : {ingressos[ingresso][2]}
Tipo    : {ingressos[ingresso][3]}
                                               ''')
                        print("_"*60)
                  input("\nTecle <ENTER> para continuar...")
                              
                        
                              
                        
                        
            elif opcao == 2:
                  os.system('cls' if os.name == 'nt' else 'clear')
                  print("_"*60)
                  print(
                        """
Exclusão de Ingressos 🎟️
                        """)
                  print("_"*60)
                  cod = int(input('\nDigite código do ingresso que deseja excluir: '))
                  ingressos = ler_arquivo('banco/ingressos.txt')
                  sessoes = ler_arquivo('banco/sessoes.txt')
                  try:
                        if ingressos[cod]:
                              sessoes[ingressos[cod][1]][2]= sessoes[ingressos[cod][1]][2]+1
                              ingressos.pop(cod)
                              escrever_arquivo("banco/sessoes.txt",sessoes)
                              escrever_arquivo('banco/ingressos.txt',ingressos)
                              print('\nIngresso excluído!\n')
                              
                  except:
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
                  filmes = ler_arquivo('banco/filmes.txt')
                  sessoes = ler_arquivo('banco/sessoes.txt')
                  if cod in ingressos:
                        cpf = input('\nDigite o cpf do usuário:')
                        for sessao in sessoes:
                             print(f'Código : {sessao}   | Filme : {filmes[sessoes[sessao][0]][0]}')
                        sessao = int(input('\nDigite o código da sessão que deseja comprar ingresso: '))      
                        valor = float(input('digite o valor do ingresso'))
                        tipo = input('Digite o tipo do ingresso: ')
                        data_hj = str(date.today())
                        ingresso = [cpf,sessao,valor,tipo,data_hj]
                        ingressos[cod]=ingresso
                        escrever_arquivo('banco/ingressos.txt',ingressos)
                              
                        print('\nIngresso editado com sucesso!\n')
                        
                        
                                    
                                    
                                    
                  else:
                        print('\nIngresso não encontrado!')
                  input("Tecle <ENTER> para continuar...")
            elif opcao == 4:
                  break
            else:
                  print('\nOpção inválida. Tente novamente.\n')
                  input("Tecle <ENTER> para continuar...")

import os
from datetime import date
from banco import *

data = str(date.today())
from config import ler_arquivo,escrever_arquivo

def sessoes():
       while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("_"*60)
            print(
                  """
            Módulo de Sessão 🎞️
                  """)
            print("_"*60)
            
            print("""
      ╔══════════════════════════════════════════════════════════╗
      ║                       MENU                               ║
      ╠══════════════════════════════════════════════════════════╣
      ║ 0 - Cadastrar Sessão                                     ║
      ║ 1 - Listar Sessão Disponivél                             ║
      ║ 2 - Excluir Sessão                                       ║
      ║ 3 - Editar Sessão                                        ║                                      
      ║ 4 - Voltar                                               ║
      ╚══════════════════════════════════════════════════════════╝
      """)
            opcao = int(input('Digite sua ação: '))
            if opcao == 0:
                  os.system('cls' if os.name == 'nt' else 'clear')
                  print("_"*60)
                  print(
                        """
Cadastro de Sessão 🎞️
                        """)
                  print("_"*60)
                  sessoes = ler_arquivo('banco/sessoes.txt')
                  cod = len(sessoes.keys()) + 1
                  print('\nMonte sua sessão!\n\nFilmes disponíveis\n')
                  filmes = ler_arquivo('banco/filmes.txt')
                  for filme in filmes:
                        print(f'Código : {filme}   | Filme : {filmes[filme][0]}')
                  filme = int(input('\nDigite o código do filme da sua sessão: '))
                  if filme in filmes:
                        print('\nSalas disponíveis\n')
                        salas = ler_arquivo('banco/salas.txt')
                        for sala in salas:
                              print(f'Código : {sala}   | Capacidade : {salas[sala][0]} ')
                        sala = int(input('\nDigite o código da sala da sua sessão: '))
                        
                        if sala in salas:
                              data = input('\nDigite a data da sessão. [00-00-0000] :')
                              inicio = float(input('Digite o horário da sessão:'))
                              duração = float(input("Digite a duração da sessão: (em horas) "))
                              valor = float(input('Digite o valor da sessão: '))
                              termino = inicio + duração
                              dis = True
                              for sessao in sessoes:
                                    if inicio<=sessoes[sessao][5] and termino>=sessoes[sessao][4] and sala==sessoes[sessao][1] and sessoes[sessao][3]==data:
                                          dis = False
                                          break
                              
                              if dis:
                                    data_hj = str(date.today())
                                    vagas = salas[sala][0]
                                    sessao = [filme,sala,vagas,data,inicio,termino,valor,data_hj]
                                    sessoes[cod]=sessao
                                    escrever_arquivo('banco/sessoes.txt',sessoes)
                                    escrever_arquivo('banco/salas.txt',salas)
                                                            
                                    print('\nSessão cadastrada com sucesso!\n')
                              else:
                                    print("Sala indispinível. Tente novamente")
                              input("Tecle <ENTER> para continuar...")
                              
                                    
                              
                              
                        else:
                              print('\nSala não cadastrada! Tente novamente.')
                              input("Tecle <ENTER> para continuar...")
                  else:
                        print('\nFilme não cadastrado! Tente novamente.')
                        input("Tecle <ENTER> para continuar...")
                        
                  
                  
            elif opcao == 1 :
                  os.system('cls' if os.name == 'nt' else 'clear')
                  print("_"*60)
                  print(
                        """
Lista de Sessão 🎞️
                        """)
                  print("_"*60)
                  print()
                  sessoes = ler_arquivo('banco/sessoes.txt')
                  salas = ler_arquivo('banco/salas.txt')
                  filmes = ler_arquivo('banco/filmes.txt')
                  for sessao in sessoes:
                        dis = sessoes[sessao][2]
                        if dis>0:
                              t = "Assentos disponiveis"
                        else:
                              t = "Esgotada"
                              
                        print(f'''
                              
Código          : {sessao}
Nome do filme   : {filmes[sessoes[sessao][0]][0]}
Sala            : {sessoes[sessao][1]}
Data            : {sessoes[sessao][3]}
Horário         : {sessoes[sessao][4]}
Valor           : {sessoes[sessao][6]}R$
Disponibilidade : {t}
                              ''')
                        print('_'*60)
                        
                  
                        
                  input("Tecle <ENTER> para continuar...")
                  
            elif opcao == 2:
                  os.system('cls' if os.name == 'nt' else 'clear')
                  print("_"*60)
                  print(
                        """
Exclusão de Sessão 🎞️
                        """)
                  print("_"*60)
                  cod = int(input('Digite código do sessão que deseja excluir: '))
                  sessoes = ler_arquivo('banco/sessoes.txt')
                  try:
                        if sessoes[cod]:
                              salas = ler_arquivo('banco/salas.txt')
                              salas[sessoes[cod][1]][2] = True
                              sessoes.pop(cod)
                              escrever_arquivo('banco/salas.txt',salas)
                              escrever_arquivo('banco/sessoes.txt',sessoes)
                              print('\nSessão excluída!\n')
                  
                  except:
                        print('\nSessão não encontrada!')
                  input("Tecle <ENTER> para continuar...")
           
            elif opcao == 3:
                  os.system('cls' if os.name == 'nt' else 'clear')
                  print("_"*60)
                  print(
                        """
Edição de Sessão 🎞️
                        """)
                  print("_"*60)
                  cod = int(input('\nDigite o codígo da sessão que deseja editar: '))
                  sessoes = ler_arquivo('banco/sessoes.txt')
                  salas = ler_arquivo('banco/salas.txt')
                  filmes = ler_arquivo('banco/filmes.txt')
                  if cod in sessoes:
                        print('\nFilmes disponíveis\n')
                        for filme in filmes:
                              print(f'Código : {filme}   | Filme : {filmes[filme][0]}')
                        filme = int(input('\nDigite o código do filme da sua sessão: '))
                        if filme in filmes:
                              print('\nSalas disponíveis\n')
                              for sala in salas:
                                    print(f'Código : {sala}   | Capacidade : {salas[sala][0]}')
                              sala = int(input('\nDigite o código da sala da sua sessão: '))
                              while True:
                                    if sala in salas and salas[sala][2] == False and sala!=sessoes[cod][1]:
                                          print("Sala indispinível. Tente novamente")
                                          sala = int(input('\nDigite o código da sala da sua sessão: '))
                                    else:
                                          break
                              if sala in salas:
                                    data = input('\nDigite a data da sessão. [00-00-0000] :')
                                    inicio = float(input('Digite o horário da sessão:'))
                                    duração = float(input("Digite a duração da sessão: (em horas) "))
                                    valor = float(input('Digite o valor da sessão: '))
                                    termino = inicio + duração
                                    data_hj = str(date.today())
                                    vagas = salas[sala][0]
                                    sessao = [filme,sala,vagas,data,inicio,termino,valor,data_hj]
                                    sessoes[cod]=sessao
                                    escrever_arquivo('banco/sessoes.txt',sessoes)
                                    escrever_arquivo('banco/salas.txt',salas)
                                    
                              else:
                                    print('Sala não cadastrada! Tente novamente.')
                                    
                        else:
                              print('Filme não cadastrado! Tente novamente.')
                        
                              
                  else:
                        print('Sessão não encontrada. Tente novamente')
                  input("Tecle <ENTER> para continuar...")
                  
            elif opcao == 4:
                  break
            else:
                  print('\nOpção inválida. Tente novamente.\n')
                  input("Tecle <ENTER> para continuar...")
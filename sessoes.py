import os
from datetime import date
from banco import *

data = str(date.today())
from config import ler_arquivo,escrever_arquivo, validar_data, definir_status

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
║ 2 - Cancelar Sessão                                      ║
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
                  exist = False
                  for filme in filmes:
                        if filmes[filme][2]:
                              exist=True
                              print(f'Código : {filme}   | Filme : {filmes[filme][0]}')
                  filme = int(input('\nDigite o código do filme da sua sessão: '))
                  if filme in filmes and filmes[filme][2]:
                        print('\nSalas disponíveis\n')
                        salas = ler_arquivo('banco/salas.txt')
                        exist_s = False
                        for sala in salas:
                              if salas[sala][2]:
                                    print(f'Código : {sala}   | Capacidade : {salas[sala][0]} ')
                                    exist_s = True
                        if not exist_s:
                              print('Sem salas ativas. Tente cadastrar uma sala')
                        else:
                              sala = int(input('\nDigite o código da sala da sua sessão: '))
                                    
                              if sala in salas and salas[sala][2]:
                                    data = input('\nDigite a data da sessão. [00-00-0000] :')
                                    validacao_data = validar_data(data)
                                    if validacao_data:
                                          inicio = float(input('Digite o horário da sessão:'))
                                          duração = float(input("Digite a duração da sessão: (em horas) "))
                                          valor = float(input('Digite o valor da sessão: '))
                                          termino = inicio + duração
                                          status,dis = True,True
                                          for sessao in sessoes:
                                                if inicio<=sessoes[sessao][5] and termino>=sessoes[sessao][4] and sala==sessoes[sessao][1] and sessoes[sessao][3]==data and sessoes[sessao][7]:
                                                      dis = False
                                                      break
                                                                  
                                          if dis:
                                                data_hj = str(date.today())
                                                vagas = salas[sala][0]
                                                sessao = [filme,sala,vagas,data,inicio,termino,valor,status,data_hj]
                                                sessoes[cod]=sessao
                                                escrever_arquivo('banco/sessoes.txt',sessoes)
                                                escrever_arquivo('banco/salas.txt',salas)
                                                                                                
                                                print('\nSessão cadastrada com sucesso!\n')
                                          else:
                                                print("Sala indispinível. Tente novamente")
                                    else:
                                          print('Data inválida! Tente novamente')
                              else:
                                    print('\nSala não cadastrada ou indisponivel! Tente novamente.')
                        
                                          
                  else:
                        print('\nFilme não cadastrado ou indisponivel! Tente novamente.')
            
                  if not exist:
                        print('Sem filmes ativos. Tente cadastrar um filme')
                        
                  
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
                        dis= sessoes[sessao][2]
                        status = definir_status(sessoes[sessao][7])
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
Valor Ingresso  : {sessoes[sessao][6]}
Disponibilidade : {t}
Status          : {status}

                              ''')
                        print('_'*60)
                        
                  
                        
                  input("Tecle <ENTER> para continuar...")
                  
            elif opcao == 2:
                  os.system('cls' if os.name == 'nt' else 'clear')
                  print("_"*60)
                  print(
                        """
Cancelamento de Sessão 🎞️
                        """)
                  print("_"*60)
                  sessao = int(input('Digite código do sessão que deseja cancelar: '))
                  sessoes = ler_arquivo('banco/sessoes.txt')
                  
                  if sessao in sessoes:
                        sessoes[sessao][7] =False
                        escrever_arquivo('banco/sessoes.txt',sessoes)
                        print('\nSessão cancelada!\n')
                  
                  else:
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
                  sessoes = ler_arquivo('banco/sessoes.txt')
                  cod = int(input('Digite o codigo da sessão que deseja editar:'))
                  exist = False
                  if cod in sessoes and sessoes[cod][7]:
                        filmes = ler_arquivo('banco/filmes.txt')
                        for filme in filmes:
                              if filmes[filme][2]:
                                    exist=True
                                    print(f'Código : {filme}   | Filme : {filmes[filme][0]}')
                        if not exist:
                              print('Sem filmes ativos. Tente cadastrar um filme')
                        else:
                              filme = int(input('\nDigite o código do filme da sua sessão: '))
                              if filme in filmes and filmes[filme][2]:
                                    print('\nSalas disponíveis\n')
                                    salas = ler_arquivo('banco/salas.txt')
                                    exist_s = False
                                    for sala in salas:
                                          if salas[sala][2]:
                                                print(f'Código : {sala}   | Capacidade : {salas[sala][0]} ')
                                                exist_s = True
                                    sala = int(input('\nDigite o código da sala da sua sessão: '))
                                                
                                    if sala in salas and salas[sala][2]:
                                          data = input('\nDigite a data da sessão. [00-00-0000] :')
                                          validacao_data = validar_data(data)
                                          if validacao_data:
                                                inicio = float(input('Digite o horário da sessão:'))
                                                duração = float(input("Digite a duração da sessão: (em horas) "))
                                                valor = float(input('Digite o valor da sessão: '))
                                                termino = inicio + duração
                                                status,dis = True,True
                                                for sessao in sessoes:
                                                      if sessao != cod:
                                                            if inicio<=sessoes[sessao][5] and termino>=sessoes[sessao][4] and sala==sessoes[sessao][1] and sessoes[sessao][3]==data:
                                                                  dis = False
                                                                  break
                                                                        
                                                if dis:
                                                      data_hj = str(date.today())
                                                      vagas = sessoes[cod][2]
                                                      sessao = [filme,sala,vagas,data,inicio,termino,valor,status,data_hj]
                                                      sessoes[cod]=sessao
                                                      escrever_arquivo('banco/sessoes.txt',sessoes)
                                                      escrever_arquivo('banco/salas.txt',salas)
                                                                                                      
                                                      print('\nSessão editada com sucesso!\n')
                                                else:
                                                      print("Sala indispinível. Tente novamente")
                                          else:
                                                print('Data inválida! Tente novamente')
                                    else:
                                          print('\nSala não cadastrada ou indisponivel! Tente novamente.')
                                    if not exist_s:
                                          print('Sem salas ativas. Tente cadastrar uma sala')
                                                
                              else:
                                    print('\nFilme não cadastrado ou indisponivel! Tente novamente.')
                  else:
                        print('Sessão não cadastrada ou inativa. Tente novamente')
                  
                  input("\nTecle <ENTER> para continuar...")
                  
                  
            elif opcao == 4:
                  break
            else:
                  print('\nOpção inválida. Tente novamente.\n')
                  input("Tecle <ENTER> para continuar...")
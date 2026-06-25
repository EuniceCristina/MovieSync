import os
from datetime import datetime, date
from banco import *

data = str(date.today())
from config import ler_arquivo,escrever_arquivo, definir_status

#relatorios : abre e mostra, pesquisa com filtros, filtros, interligação

def relatorios():
      while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("_"*60)
            print(
                  """
Módulo de Relatórios 📋 
                  """)
            print("_"*60)
            print("""
╔══════════════════════════════════════════════════════════╗
║                       MENU                               ║
╠══════════════════════════════════════════════════════════╣
║ 0 - Relátorios de Usuários                               ║
║ 1 - Relatórios de Filmes Em Cartaz                       ║
║ 2 - Relátorios de Ingressos                              ║
║ 3 - Voltar                                               ║
╚══════════════════════════════════════════════════════════╝
      """)
            opcao = int(input('Digite sua ação: '))
            if opcao==0:
                  stop = True
                  while stop:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("_"*60)
                        print(
                              """
Relatórios de Usuários 📋 
                              """)
                        print("_"*60)
                        print("""
╔══════════════════════════════════════════════════════════╗
║                       MENU                               ║
╠══════════════════════════════════════════════════════════╣
║ 0 - Listar Usuários                                      ║
║ 1 - Usuários Inativos                                    ║
║ 2 - Pesquisar Usuário                                    ║
║ 3 - Usuário com sessões futuras                          ║
║ 4 - Voltar                                               ║
╚══════════════════════════════════════════════════════════╝
                  """)
                        opcao = int(input('Digite sua ação: '))
                        usuarios = ler_arquivo('banco/usuarios.txt')
                        if opcao == 0: 
                              os.system('cls' if os.name == 'nt' else 'clear')
                              print("_"*60)
                              print(
                              """
Listagem de Usuários 👤
                              """)
                              print("_"*60)
                              
                              for usuario in usuarios:
                                    status = definir_status(usuarios[usuario][3])
                                    print(f'''
{list(usuarios.keys()).index(usuario)+1}°

Nome  : {usuarios[usuario][0]}
CPF   : {usuario}
Email : {usuarios[usuario][1]}
Status: {status}
                                          ''')
                                    print("_"*60)
                              input("\nTecle <ENTER> para continuar...")
                        
                        elif opcao == 1:
                              os.system('cls' if os.name == 'nt' else 'clear')
                              print("_"*60)
                              print(
                              """
      Usuários Inativos 👤
                              """)
                              print("_"*60)
                              
                              for usuario in usuarios:
                                    if not usuarios[usuario][3]:
                                          print(f'''
{list(usuarios.keys()).index(usuario)+1}°

Nome  : {usuarios[usuario][0]}
CPF   : {usuario}
Email : {usuarios[usuario][1]}
                                                ''')
                                          print("_"*60)
                              input("\nTecle <ENTER> para continuar...") 
                  
                        
                              
                        
                        elif opcao==2:
                              os.system('cls' if os.name == 'nt' else 'clear')
                              print("_"*60)
                              print(
                              """
Buscar de Usuários 👤
                              """)
                              print("_"*60)
                              nome = input('Digite o nome do usuário que deseja buscar:').lower()
                              print("""
                                    
Resultados encontrados: 
                                    
                                    """)
                              for usuario in usuarios:
                                    if (usuarios[usuario][0].lower()).startswith(nome) or (usuarios[usuario][0].lower())==nome:
                                          if usuarios[usuario][3]:
                                                dis = 'Ativo'
                                          else:
                                                dis = 'Inativo'
                                          print(f'''
{list(usuarios.keys()).index(usuario)+1}°

Nome  : {usuarios[usuario][0]}
CPF   : {usuario}
Email : {usuarios[usuario][1]}
Status: {dis}
                                                ''')
                                          print("_"*60)
                              input("\nTecle <ENTER> para continuar...")
                        
                        elif opcao == 3:
                              
                              sessoes = ler_arquivo('banco/sessoes.txt')
                              filmes = ler_arquivo('banco/filmes.txt')
                              ingressos = ler_arquivo('banco/ingressos.txt')
                              os.system('cls' if os.name == 'nt' else 'clear')
                              print("_"*60)
                              print(
                              """
Usuários com sessões futuras 👤
                              """)
                              print("_"*60)
                              for usuario in usuarios:
                                    for ingresso in ingressos:
                                          
                                          if ingressos[ingresso][0] ==usuario:
                                                
                                                for sessao in sessoes:
                                                      if ingressos[ingresso][1]==sessao:
                                                            data_sessao = datetime.strptime(
                                                                  sessoes[sessao][3],
                                                                  "%d-%m-%Y"
                                                                  ).date()
                                                            hoje = date.today()
                                                            if data_sessao>=hoje:
                                                                  print(f'''
{list(usuarios.keys()).index(usuario)+1}°                                                                        

Nome  : {usuarios[usuario][0]}
Sessao: {sessao}
Filme : {filmes[sessoes[sessao][0]][0]}
                                                            ''')
                                                                  print("_"*60)
                              input("\nTecle <ENTER> para continuar...")
                                                      
                                                
                              
                              
                              
                                    
                        elif opcao == 4:
                              stop = False
                        
                        
                        
                        
                  
                  
            
            
            elif opcao == 1:
                  stop = True
                  while stop:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("_"*60)
                        print(
                              """
Relátório de Filmes  🎞️ 
                              """)
                        print("_"*60)
                        print("""
╔══════════════════════════════════════════════════════════╗
║                       MENU                               ║
╠══════════════════════════════════════════════════════════╣
║ 0 - Listar Filmes                                        ║
║ 1 - Filmes Inativos                                      ║
║ 2 - Pesquisar Filmes                                     ║
║ 3 - Filmes com sessões futuras                           ║
║ 4 - Voltar                                               ║
╚══════════════════════════════════════════════════════════╝
                  """)
                        opcao = int(input('Digite sua ação: '))
                        filmes = ler_arquivo('banco/filmes.txt')
                        if opcao == 0: 
                              os.system('cls' if os.name == 'nt' else 'clear')
                              print("_"*60)
                              print(
                              """
Listagem de Filmes 🎞️
                              """)
                              print("_"*60)
                              
                              for filme in filmes:
                                    status = definir_status(filmes[filme][2])
                                    print(f'''
Código          : {filme}         
Nome            : {filmes[filme][0]}
Gênero          : {filmes[filme][1]}
Status          : {status}
                                          ''')
                                    print("_"*60)
                              input("\nTecle <ENTER> para continuar...")
                        
                        elif opcao == 1:
                              os.system('cls' if os.name == 'nt' else 'clear')
                              print("_"*60)
                              print(
                              """
Filmes Inativos 🎞️
                              """)
                              print("_"*60)
                              
                              for filme in filmes:
                                    if not filmes[filme][2]:
                                          print(f'''
Código          : {filme}         
Nome            : {filmes[filme][0]}
Gênero          : {filmes[filme][1]}
                                                ''')
                                          print("_"*60)
                              input("\nTecle <ENTER> para continuar...") 
                  
                        
                              
                        
                        elif opcao==2:
                              os.system('cls' if os.name == 'nt' else 'clear')
                              print("_"*60)
                              print(
                              """
Buscar de Filmes 🎞️
                              """)
                              print("_"*60)
                              nome = input('Digite o nome do filmes que deseja buscar:').lower()
                              print("""
                                    
Resultados encontrados: 
                                    
                                    """)
                              exist = False
                              for filme in filmes:
                                    if (filmes[filme][0].lower()).startswith(nome) or (filmes[filme][0].lower())==nome:
                                          exist = True
                                          status=definir_status(filmes[filme][2])
                                          print(f'''
Código          : {filme}         
Nome            : {filmes[filme][0]}
Gênero          : {filmes[filme][1]}
Status          : {status}
                                                ''')
                                          print("_"*60)
                              if not exist:
                                    print('Filme não encontrado!')
                              input("\nTecle <ENTER> para continuar...")
                        
                        elif opcao == 3:
                              
                              sessoes = ler_arquivo('banco/sessoes.txt')
                              filmes = ler_arquivo('banco/filmes.txt')
                              os.system('cls' if os.name == 'nt' else 'clear')
                              print("_"*60)
                              print(
                              """
Filmes com sessões futuras 🎞️
                              """)
                              print("_"*60)
                              exist=False
                              for filme in filmes:
                                    for sessao in sessoes:
                                          status = definir_status(filmes[filme][2])
                                          if sessoes[sessao][0]==filme and sessoes[sessao][7]:
                                                 exist=True
                                                 print(f'''
Código          : {filme}         
Nome            : {filmes[filme][0]}
Gênero          : {filmes[filme][1]}
Status          : {status}
                                                            ''')
                                                 print("_"*60)
                              if not exist:
                                    print('Sem filmes com sessões futuras.')
                              input("\nTecle <ENTER> para continuar...")
                                                      
                                                
                              
                              
                              
                                    
                        elif opcao == 4:
                              stop = False
                  
            
                   
            elif opcao == 2:
                  stop = True
                  while stop:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("_"*60)
                        print(
                              """
Relátório de Salas  🎞️ 
                              """)
                        print("_"*60)
                        print("""
╔══════════════════════════════════════════════════════════╗
║                       MENU                               ║
╠══════════════════════════════════════════════════════════╣
║ 0 - Listar Salas                                         ║
║ 1 - Salas Inativos                                       ║
║ 2 - Pesquisar Salas                                      ║
║ 3 - Salas com sessões futuras                            ║
║ 4 - Voltar                                               ║
╚══════════════════════════════════════════════════════════╝
                  """)
                        opcao = int(input('Digite sua ação: '))
                        salas = ler_arquivo('banco/salas.txt')
                        if opcao == 0: 
                              os.system('cls' if os.name == 'nt' else 'clear')
                              print("_"*60)
                              print(
                              """
Listagem de Salas 🎞️
                              """)
                              print("_"*60)
                              
                              for sala in salas:
                                    status = definir_status(salas[sala][2])
                                    print(f'''
Código          : {sala}
Capacidade      : {salas[sala][0]}
Tipo            : {salas[sala][1]}
status          : {status}
                                          ''')
                                    print("_"*60)
                              input("\nTecle <ENTER> para continuar...")
                        
                        elif opcao == 1:
                              os.system('cls' if os.name == 'nt' else 'clear')
                              print("_"*60)
                              print(
                              """
Salas Inativas 🎞️
                              """)
                              print("_"*60)
                              
                              for sala in salas:
                                    if not salas[sala][2]:
                                          print(f'''
Código          : {sala}
Capacidade      : {salas[sala][0]}
Tipo            : {salas[sala][1]}

                                                ''')
                                          print("_"*60)
                              input("\nTecle <ENTER> para continuar...") 
                  
                        
                              
                        
                        elif opcao==2:
                              os.system('cls' if os.name == 'nt' else 'clear')
                              print("_"*60)
                              print(
                              """
Buscar de Salas 🎞️
                              """)
                              print("_"*60)
                              tipo = input('Digite o tipo de sala que deseja buscar:').lower()
                              print("""
                                    
Resultados encontrados: 
                                    
                                    """)
                              exist = False
                              for sala in salas:
                                    if (salas[sala][1].lower()).startswith(tipo) or (salas[sala][1].lower())==tipo:
                                          exist = True
                                          status=definir_status(salas[sala][2])
                                          print(f'''
Código          : {sala}
Capacidade      : {salas[sala][0]}
Tipo            : {salas[sala][1]}
status          : {status}
                                                ''')
                                          print("_"*60)
                              if not exist:
                                    print('Sala não encontrado!')
                              input("\nTecle <ENTER> para continuar...")
                        
                        elif opcao == 3:
                              
                              sessoes = ler_arquivo('banco/sessoes.txt')
                              salas = ler_arquivo('banco/salas.txt')
                              os.system('cls' if os.name == 'nt' else 'clear')
                              print("_"*60)
                              print(
                              """
Salas com sessões futuras 
                              """)
                              print("_"*60)
                              exist=False
                              for sala in salas:
                                    for sessao in sessoes:
                                          status = definir_status(salas[sala][2])
                                          if sessoes[sessao][0]==sala and sessoes[sessao][7]:
                                                 exist=True
                                                 print(f'''
Código          : {sala}
Capacidade      : {salas[sala][0]}
Tipo            : {salas[sala][1]}
status          : {status}
                                                            ''')
                                                 print("_"*60)
                              if not exist:
                                    print('Sem salas com sessões futuras.')
                              input("\nTecle <ENTER> para continuar...")
                                                      
                                                
                              
                              
                              
                                    
                        elif opcao == 4:
                              stop = False
                        
                              input("Tecle <ENTER> para continuar...")
                        else:
                              print('\nOpção inválida. Tente novamente.\n')
                              input("Tecle <ENTER> para continuar...")

            elif opcao == 3:
                  break
            else:
                  print('\nOpção inválida. Tente novamente.\n')
                  input("Tecle <ENTER> para continuar...")
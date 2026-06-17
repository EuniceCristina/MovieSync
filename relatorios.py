import os
from datetime import date
from banco import *

data = str(date.today())
from config import ler_arquivo,escrever_arquivo

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
                  print()
                  print(
                  """
            Relátório de Usuários
                  """)
                  print("_"*60)
                  print()
                  usuarios = ler_arquivo('banco/usuarios.txt')
                  print(f'Total de usuários cadastrados: {len(usuarios)}')
                  print('\nUsuários cadastrados hoje:')
                  data = str(date.today())
                  cont = 0
                  for usuario in usuarios:
                        if usuarios[usuario][3]==data:
                              cont+=1
                  print(f'\nUsuários cadastrados hoje: {cont}')
                  print()
                  primeiro = list(usuarios.keys())[0]
                  ultimo = list(usuarios.keys())[-1]
                  print(f'''
                  Nome  : {usuarios[primeiro][0]}
                  CPF   : {primeiro}
                  Email : {usuarios[primeiro][1]}
                                    ''')
                  print("\nÚltimo usuário cadastrado: ")
                  print(f'''
                  Nome  : {usuarios[ultimo][0]}
                  CPF   : {ultimo}
                  Email : {usuarios[ultimo][1]}\n
                                    ''')
                  input("\nTecle <ENTER> para continuar...")
            
            
            elif opcao == 1:
                  print()
                  print(
                  """
            Relátório de Filmes
                  """)
                  print("_"*60)
                  print()
                  filmes = ler_arquivo('banco/filmes.txt')
                  print(f'Total de filmes cadastrados: {len(filmes.keys())}\n')
                  cartaz, ind,acao,drama,com,terror = 0,0,0,0,0,0
                  for filme in filmes:
                        if filmes[filme][2]:
                              cartaz +=1
                        else:
                              ind +=1
                        if filmes[filme][1].lower() == 'ação':
                              acao+=1
                        elif filmes[filme][1].lower() == 'drama':
                              drama+=1
                        elif filmes[filme][1].lower() == 'terror':
                              terror+=1
                        elif filmes[filme][1].lower() == 'comédia':
                              com+=1
                  print(f'Filmes em cartaz    : {cartaz}')
                  print(f'Filmes indisponíveis : {ind} ')
                  print()
                  print('Contagem por gênero ')
                  print(f'Ação    : {acao}')
                  print(f'Drama   : {drama}')
                  print(f'Terror  : {terror}')
                  print(f'Comédia : {com}')
                  print()
                  input("Tecle <ENTER> para continuar...") 
            elif opcao == 2:
                  print()
                  print(
                  """
            Relátório de Ingressos
                  """)
                  print("_"*60)
                  print()
                  ingressos = ler_arquivo('banco/ingressos.txt')
                  print(f'Total de ingressos cadastrados: {len(ingressos.keys())}\n')
                  data = str(date.today())
                  cont=0
                  for ingresso in ingressos:
                        if ingressos[ingresso][4] == data:
                              cont+=1
                  print(f'Total de ingressos cadastrados hoje:{cont}\n')
                  input("\nTecle <ENTER> para continuar...") 
            elif opcao == 3:
                  break
            else:
                  print('\nOpção inválida. Tente novamente.\n')
                  input("Tecle <ENTER> para continuar...")
                  
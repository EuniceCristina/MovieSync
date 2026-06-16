import os
from datetime import date
from banco import *

data = str(date.today())


def ler_arquivo(arquivo):
      arquivo = open(arquivo,'r')
      usuarios = eval(arquivo.read())
      arquivo.close()
      return usuarios

def escrever_arquivo(arquivo,usuarios):
      arquivo = open(arquivo,'w')
      arquivo.write(str(usuarios))
      arquivo.close()
      
lista_usuarios = ler_arquivo('banco/usuarios.txt')
lista_filmes = ler_arquivo('banco/filmes.txt')
lista_salas = ler_arquivo('banco/salas.txt')
lista_sessoes = ler_arquivo('banco/sessoes.txt')
lista_ingressos = ler_arquivo('banco/ingressos.txt')

def usuarios():
      
      
      while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("_"*60)
            print(
                  """
      Módulo de Usuários 👤
                  """)
            print("_"*60)
            
            print("""
╔══════════════════════════════════════════════════════════╗
║                       MENU                               ║
╠══════════════════════════════════════════════════════════╣
║ 0 - Cadastrar Usuários                                   ║
║ 1 - Listar Usuários                                      ║
║ 2 - Excluir Usuário                                      ║
║ 3 - Editar Usuário                                       ║                                      
║ 4 - Voltar                                               ║
╚══════════════════════════════════════════════════════════╝
""")
            opcao = int(input('Digite sua ação: '))
            if opcao == 0:
                  usuarios = ler_arquivo('banco/usuarios.txt')
                  os.system('cls' if os.name == 'nt' else 'clear')
                  print("_"*60)
                  print(
                  """
 Cadastro de Usuários 👤
                  """)
                  print("_"*60)
                  nome = input('\nDigite o nome do usuario: ')
                  cpf = input('Digite o cpf do usuario : ')
                  
                  if cpf in usuarios:
                        print('Cpf já cadastrado. Tente novamente.')
                  else:
                        email = input('Digite um email do usuário: ')
                        senha = input('Digite uma senha : ')
                        data = str(date.today())
                        pessoa = [nome,email,senha,data]
                        
                        usuarios[f'{cpf}']=pessoa
                        escrever_arquivo('banco/usuarios.txt',usuarios)
                  

                  
                        print('\nUsuário cadastrado com sucesso!\n')
                  input("Tecle <ENTER> para continuar...")
            elif opcao == 1 :
                  os.system('cls' if os.name == 'nt' else 'clear')
                  print("_"*60)
                  print(
                  """
 Listagem de Usuários 👤
                  """)
                  print("_"*60)
                  usuarios = ler_arquivo('banco/usuarios.txt')
                  
                  for usuario in usuarios:
                        print(f'''
{list(usuarios.keys()).index(usuario)+1}°

Nome  : {usuarios[usuario][0]}
CPF   : {usuario}
Email : {usuarios[usuario][1]}
                              ''')
                        print("_"*60)
                  
                  
            
                  
                  input("Tecle <ENTER> para continuar...")
            
            elif opcao == 2:
                  os.system('cls' if os.name == 'nt' else 'clear')
                  print("_"*60)
                  print(
                  """
 Exclusão de Usuários 👤
                  """)
                  print("_"*60)
                  usuarios = ler_arquivo('banco/usuarios.txt')
                  cpf = input('\nDigite cpf do usuário que deseja excluir: ')
                  ingressos = ler_arquivo('banco/ingressos.txt') 
                  if cpf in usuarios:
                        if cpf in ingressos:
                              print('\nUsuário possui ingressos comprados.')
                        else:
                              usuarios.pop(cpf)
                              escrever_arquivo('banco/usuarios.txt',usuarios)
                        
                        print('\nUsuário excluído!\n')
                        
                 
                  else:
                        print('\nUsuário não encontrado!')
                  
                  
                  input("Tecle <ENTER> para continuar...")
                  
            
            elif opcao == 3:
                  os.system('cls' if os.name == 'nt' else 'clear')
                  print("_"*60)
                  print(
                  """
 Edição de Usuários 👤
                  """)
                  print("_"*60)
                  cpf = input('\nDigite o cpf do usuario que deseja editar: ')
                  usuarios = ler_arquivo('banco/usuarios.txt')
                  if cpf in usuarios:
                        nome = input('Digite o nome do usuario: ')
                        email = input('Digite um email do usuário: ')
                        senha = input('Digite uma senha : ')
                        
                        nov_usuario = [nome,email,senha,usuarios[cpf][3]]
                        usuarios[f'{cpf}'] = nov_usuario
                        escrever_arquivo('banco/usuarios.txt',usuarios)
                        print('\nUsuário editado com sucesso!\n')
                        
                        
                        
                  else:
                        print('\nUsuário não encontrado!')
                  input("Tecle <ENTER> para continuar...")
            elif opcao == 4:
                  break
            else:
                  print('\nOpção inválida. Tente novamente.\n')
                  input("Tecle <ENTER> para continuar...")
def filmes():
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
      ║ 2 - Excluir Filme                                        ║
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
                  dis = True
                  filme = [nome,genero,dis]
                  lista_filmes[cod]=filme
                  escrever_arquivo('banco/filmes.txt',lista_filmes)
                        
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
                        dis = lista_filmes[filme][2]
                        if dis:
                              t = "Em cartaz"
                        else:
                              t = "Indísponivel"
                              
                        print(f'''

Código          : {filme}         
Nome            : {filmes[filme][0]}
Gênero          : {filmes[filme][1]}
Disponibilidade : {t}
                              ''')
                        print("_"*60)
            
                        
                  
                        
                  input("Tecle <ENTER> para continuar...")
                  
            elif opcao == 2:
                  os.system('cls' if os.name == 'nt' else 'clear')
                  print("_"*60)
                  print(
                  """
Exclusão de Filmes 🎞️
                  """)
                  print("_"*60)
                  cod = int(input('\nDigite código do filme que deseja excluir: '))
                  filmes = ler_arquivo('banco/filmes.txt')
                  sessoes = ler_arquivo('banco/sessoes.txt')
                  exist = False
                  try :
                        if filmes[cod]:
                              for sessao in sessoes:
                                    if sessoes[sessao][0]==cod:
                                          exist = True
                              if exist:
                                    print('Filme possui sessões cadastradas.')
                              else:
                                    filmes.pop(cod)
                                    escrever_arquivo('banco/filmes.txt',filmes)
                                    print('\nFilme excluído!\n')
                  
                  except:
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
                  if filmes[cod]:
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
                        if filmes[cod][2]:
                              status = 'disponivel'
                        else:
                              status = 'não disponivel'
                        dis = input(f'Seu filme está {status}. Deseja trocar? [S/N] :').upper()
                        if dis=='S':
                              dis = not filmes[cod][2]
                        else:
                              dis =  filmes[cod][2]
                        nov_filme = [nome,genero,dis]
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
                  lista_salas[cod]=sala
                  escrever_arquivo('banco/salas.txt',lista_salas)
                        
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
                        print('\nSala não encontrado!')
                  input("\nTecle <ENTER> para continuar...")
            elif opcao == 4:
                  break
            else:
                  print('\nOpção inválida. Tente novamente.\n')
                  input("\nTecle <ENTER> para continuar...")
      
      
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
                              print(f'Código : {sala}   | Capacidade : {sessoes[sala][2]} ')
                        sala = int(input('\nDigite o código da sala da sua sessão: '))
                        while True:
                              if sala in salas and salas[sala][2] ==False:
                                    print("Sala indispinível. Tente novamente")
                                    sala = int(input('\nDigite o código da sala da sua sessão: '))
                              else:
                                    break
                        if sala in salas:
                              data = input('\nDigite a data da sessão: ')
                              hora = input('Digite o horário da sessão: ')
                                          
                              data_hj = str(date.today())
                              vagas = salas[sala][0]
                              sessao = [filme,sala,vagas,data,hora,data_hj]
                              lista_sessoes[cod]=sessao
                              escrever_arquivo('banco/sessoes.txt',lista_sessoes)
                              salas[sala][2] = False
                              escrever_arquivo('banco/salas.txt',salas)
                                                      
                              print('\nSessão cadastrada com sucesso!\n')
                              input("Tecle <ENTER> para continuar...")
                              break
                                    
                              
                              
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
                              escrever_arquivo('salas.txt',salas)
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
                              data = input('\nDigite a data da sessão: ')
                              hora = input('Digite o horário da sessão: ')
                                          
                              data_hj = str(date.today())
                              vagas = salas[sala][0]
                              salas[sessoes[cod][1]][2] = True
                              sessao = [filme,sala,vagas,data,hora,data_hj]
                              sessoes[cod]=sessao
                              escrever_arquivo('banco/sessoes.txt',sessoes)
                              salas[sala][2] = False
                              escrever_arquivo('banco/salas.txt',salas)
                                          
                              print('\nSessão editada com sucesso!\n')
                              input("Tecle <ENTER> para continuar...")
                        else:
                              print('Sala não cadastrada! Tente novamente.')
                              input("Tecle <ENTER> para continuar...")
                  else:
                        print('Filme não cadastrado! Tente novamente.')
                        input("Tecle <ENTER> para continuar...")
            elif opcao == 4:
                  break
            else:
                  print('\nOpção inválida. Tente novamente.\n')
                  input("Tecle <ENTER> para continuar...")
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
                  if ingressos[cod]:
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
                  

            
            
            
            
      

def sobre_sistema():
      os.system('cls' if os.name == 'nt' else 'clear')
      print("_"*60)
      print(
             """
      Sobre o Sistema 💻
            """)
      print("_"*60)
      print("""
Projeto de Gestão de um Cinema
            
Equipe de desenvolvimento:     
      Eunice Cristina 
      @cristinaeunice820@gmail.com

Projeto focado na gestão de cinemas a fim de melhorar a eficiência \n de atendimento e entrega de serviço
                    
                  
            """)
      input("Tecle <ENTER> para continuar...")  

            
            
            
            
      
            
      

chave = 'S'


while chave=='S':
      os.system('cls' if os.name == 'nt' else 'clear')
      print("_"*60)
      mensagem = (r"""
                                        
|  \/  |              (_)       / ____|
| \  / |  ___  __   __ _   ___ | (___   _   _  _ __    ___
| |\/| | / _ \ \ \ / /| | / _ \ \___ \ | | | || '_ \  / __|
| |  | || (_) | \ V / | ||  __/ ____) || |_| || | | || (__
|_|  |_| \___/   \_/  |_| \___||_____/  \__, ||_| |_| \___|
                                         __/ |
                                        |___/

            """)
      print(f"{mensagem}")
      print("_"*60)
      
    
      print("""
╔══════════════════════════════════════════════════════════╗
║                       MENU PRINCIPAL                     ║
╠══════════════════════════════════════════════════════════╣
║ 0 - Módulo de Usuários                                   ║
║ 1 - Módulo de Filmes                                     ║
║ 2 - Módulo de Salas                                      ║
║ 3 - Módulo de Sessões                                    ║
║ 4 - Módulo de Ingressos                                  ║
║ 5 - Módulo de Relatórios                                 ║
║ 6 - Sobre o Sistema                                      ║
║ 7 - Sair                                                 ║
╚══════════════════════════════════════════════════════════╝
""")
      opcao = int(input('Escolha o módulo que deseja acessar. [0-8] :'))
      print()

      if opcao == 7:
            chave = 'N'
            print('\nAté a próxima.')
            
      
      elif opcao == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("_"*60)
            print(
            """
      Módulo de Usuários
            """)
            print("_"*60)
            
            usuarios()
            
      
      elif opcao == 1:
            filmes()
      
      elif opcao == 2:
            salas()
      
      elif opcao == 3:
            sessoes()
            
      
      elif opcao == 4:
            ingressos()
      
      elif opcao == 5:
            relatorios()
            
      elif opcao==6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("_"*60)
            print(
                  """
            Sobre o Sistema
                  """)
            print("_"*60)
            print("""
            Projeto de Gestão de um Cinema
            
            Equipe de desenvolvimento:     
                  Eunice Cristina 
                  @cristinaeunice820@gmail.com
                    
                  
                  """)
            input("Tecle <ENTER> para continuar...")
      else:
            
            print('\nOpção inválida. Tente novamente.\n')
            input("Tecle <ENTER> para continuar...")
      
            
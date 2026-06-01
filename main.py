import os
lista_usuarios = []

def usuarios():
      global lista_usuarios
      
      chave = 'S'
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
║ 2 - Excluir Usuário                                 ║
║ 3 - Editar Usuário                                       ║                                      
║ 4 - Voltar                                               ║
╚══════════════════════════════════════════════════════════╝
""")
            opcao = int(input('Digite sua ação: '))
            if opcao == 0:
                  nome = input('Digite o nome do usuario: ')
                  cpf = input('Digite o cpf do usuario : ')
                  email = input('Digite um email do usuário: ')
                  senha = input('Digite uma senha : ')
                  usuario = [nome,cpf,email,senha]
                  lista_usuarios.append(usuario)
                  print('\nUsuário cadastrado com sucesso!\n')
                  input("Tecle <ENTER> para continuar...")
            elif opcao == 1 :
                  print(
                  """
            Lista de usuários
                  """)
                  print("_"*60)
                  print()
                  for usuario in lista_usuarios:
                        print(f'''
            Nome : {usuario[0]}
            Email : {usuario[2]}
                              ''')
                  input("Tecle <ENTER> para continuar...")
            
            elif opcao == 2:
                  cpf = input('Digite cpf do usuário que deseja excluir: ')
                  encontrado = False
                  for usuario in lista_usuarios:
                        if cpf == usuario[1]:
                              encontrado = True
                              break
                  if encontrado:
                        for usuario in lista_usuarios:
                              if cpf==usuario[1]:
                                    lista_usuarios.remove(usuario)
                                    print('Usuário excluído!\n')
                  else:
                        print('\nUsuário não encontrado!')
                  input("Tecle <ENTER> para continuar...")
            
            elif opcao == 3:
                  cpf = input('Digite o cpf do usuario que deseja editar: ')
                  encontrado = False
                  for usuario in lista_usuarios:
                        if cpf == usuario[1]:
                              encontrado = True
                              break
                  if encontrado:
                        nome = input('Digite o nome do usuario: ')
                        nov_cpf = input('Digite o cpf do usuario : ')
                        email = input('Digite um email do usuário: ')
                        senha = input('Digite uma senha : ')
                        nov_usuario = [nome,nov_cpf,email,senha]
                        for i in range(len(lista_usuarios)):
                              if lista_usuarios[i][1] == cpf:
                                    lista_usuarios[i] = nov_usuario
                                    print('\nUsuário editado com sucesso!\n')
                                    break
                        
                        
                        
                  else:
                        print('\nUsuário não encontrado!')
                  input("Tecle <ENTER> para continuar...")
            elif opcao == 4:
                  break

def filmes():
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
      

def ingressos():
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

def relatorios():
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
║ 0 - Relatórios de Ingressos                              ║
║ 1 - Relatórios de Filmes Em Cartaz                       ║
║ 2 - Relátorios de Usuários                               ║                                                                            
║ 3 - Voltar                                               ║
╚══════════════════════════════════════════════════════════╝
""")
      opcao = int(input('Digite sua ação: '))

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
║ 2 - Módulo de Ingressos                                  ║
║ 3 - Módulo de Relatórios                                 ║
║ 4 - Sobre o Sistema                                      ║
║ 5 - Sair                                                 ║
╚══════════════════════════════════════════════════════════╝
""")
      opcao = int(input('Escolha o módulo que deseja acessar. [0-8] :'))
      print()

      if opcao == 5:
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
            ingressos()
            
      
      elif opcao == 3:
            relatorios()
      
      elif opcao == 4:
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
      
            

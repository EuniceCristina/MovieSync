import os
from datetime import date
data = date.today()
lista_usuarios = {
      0 : ['Eunice','eunice@gmail.com','123',data]
}

lista_filmes = {
      0 : ['Malevola', 'drama' , 'True']
}

lista_ingressos = {}

lista_sessoes = {
      0 : [0,12,'12-12-12','12h','12',data]
}

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
                  nome = input('Digite o nome do usuario: ')
                  cpf = int(input('Digite o cpf do usuario : '))
                  email = input('Digite um email do usuário: ')
                  senha = input('Digite uma senha : ')
                  data = date.today()
                  pessoa = [nome,email,senha,data]
                  lista_usuarios[cpf]=pessoa
                  
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
            Nome  : {lista_usuarios[usuario][0]}
            CPF   : {usuario}
            Email : {lista_usuarios[usuario][1]}
                              ''')
                  
            
                  
                  input("Tecle <ENTER> para continuar...")
            
            elif opcao == 2:
                  cpf = input('Digite cpf do usuário que deseja excluir: ')
                  if cpf in lista_usuarios:
                        lista_usuarios.pop(cpf)
                        print('Usuário excluído!\n')
                 
                  else:
                        print('\nUsuário não encontrado!')
                  input("Tecle <ENTER> para continuar...")
            
            elif opcao == 3:
                  cpf = input('Digite o cpf do usuario que deseja editar: ')
                  if cpf in lista_usuarios:
                        nome = input('Digite o nome do usuario: ')
                        email = input('Digite um email do usuário: ')
                        senha = input('Digite uma senha : ')
                        
                        nov_usuario = [nome,email,senha,lista_usuarios[cpf][3]]
                        lista_usuarios[cpf] = nov_usuario
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
                  nome = input('Digite o nome do seu filme: ')
                  cod = len(lista_filmes.keys()) + 1
                  genero = input('Digite o gênero do seu filme: ')
                  dis = True
                  filme = [nome,genero,dis]
                  lista_filmes[cod]=filme
                        
                  print('\nFilme cadastrado com sucesso!\n')
                  input("Tecle <ENTER> para continuar...")
                  
            elif opcao == 1 :
                  print(
                  """
            Lista de filmes
                  """)
                  print("_"*60)
                  print()
                  for filme in lista_filmes:
                        dis = lista_filmes[filme][2]
                        if dis:
                              t = "Em cartaz"
                        else:
                              t = "Indísponivel"
                              
                        print(f'''
            Nome            : {lista_filmes[filme][0]}
            Gênero          : {lista_filmes[filme][1]}
            Disponibilidade : {t}
                              ''')
                        
                  
                        
                  input("Tecle <ENTER> para continuar...")
                  
            elif opcao == 2:
                  cod = input('Digite código do filme que deseja excluir: ')

                  if lista_filmes[cod]:
                        lista_filmes.pop(cod)
                        print('Filme excluído!\n')
                  
                  else:
                        print('\nFilme não encontrado!')
                  input("Tecle <ENTER> para continuar...")
           
            elif opcao == 3:
                  cod = input('Digite o cod do filme que deseja editar: ')
                  if lista_filmes[cod]:
                        nome = input('Digite o nome do filme: ')
                        genero = input('Digite o gênero do filme: ')
                        if lista_filmes[cod][2]:
                              status = 'disponivel'
                        else:
                              status = 'não disponivel'
                        dis = input(f'Seu filme está {status}. Deseja trocar? [S/N] :').upper()
                        if dis=='S':
                              dis = not lista_filmes[cod][2]
                        else:
                              dis =  lista_filmes[cod][2]
                        nov_filme = [nome,genero,dis]
                        lista_filmes[cod] = nov_filme
                        print('\nFilme editado com sucesso!\n')
                              
                              
                              
                  else:
                        print('\nFilme não encontrado!')
                        input("Tecle <ENTER> para continuar...")
            elif opcao == 4:
                  break
            else:
                  print('\nOpção inválida. Tente novamente.\n')
                  input("Tecle <ENTER> para continuar...")
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
      ║ 0 - Cadastrar Sessão                                    ║
      ║ 1 - Listar Sessão Disponivél                              ║
      ║ 2 - Excluir Sessão                                        ║
      ║ 3 - Editar Sessão                                         ║                                      
      ║ 4 - Voltar                                               ║
      ╚══════════════════════════════════════════════════════════╝
      """)
            opcao = int(input('Digite sua ação: '))
            if opcao == 0:
                  cod = len(lista_sessoes.keys()) + 1
                  print('\nMonte sua sessão!\n\nFilmes disponíveis\n')
                  for filme in lista_filmes:
                        print(f'Código : {filme}   | Filme : {lista_filmes[filme][0]}')
                  filme = int(input('\nDigite o código do filme da sua sessão: '))
                  if filme in lista_filmes:
                        sala = int(input('Digite o código da sala : '))
                        data = input('Digite a data da sessão: ')
                        hora = input('Digite o horário da sessão: ')
                        q_ass = int(input('Digite a quantidade de assentos: '))
                        data_hj = date.today()
                        sessao = [filme,sala,data,hora,q_ass,data_hj]
                        lista_sessoes[cod]=sessao
                                    
                        print('\nSessão cadastrada com sucesso!\n')
                  else:
                        print('Filme não cadastrado! Tente novamente.')
                        
                  input("Tecle <ENTER> para continuar...")
                  
            elif opcao == 1 :
                  print(
                  """
            Lista de sessões
                  """)
                  print("_"*60)
                  print()
                  for sessao in lista_sessoes:
                        dis = lista_sessoes[sessao][4]
                        if dis>0:
                              t = "Assentos disponiveis"
                        else:
                              t = "Esgotada"
                              
                        print(f'''
            Código          : {sessao}
            Nome do filme   : {lista_filmes[lista_sessoes[sessao][0]][0]}
            Sala            : {lista_sessoes[sessao][1]}
            Data            : {lista_sessoes[sessao][2]}
            Horário         : {lista_sessoes[sessao][3]}
            Disponibilidade : {t}
                              ''')
                        
                  
                        
                  input("Tecle <ENTER> para continuar...")
                  
            elif opcao == 2:
                  cod = input('Digite código do sessão que deseja excluir: ')

                  if lista_sessoes[cod]:
                        lista_sessoes.pop(cod)
                        print('Sessão excluída!\n')
                  
                  else:
                        print('\nSessão não encontrada!')
                  input("Tecle <ENTER> para continuar...")
           
            elif opcao == 3:
                  cod = input('Digite o cod da sessão que deseja editar: ')
                  if lista_filmes[cod]:
                        filme = int(input('\nDigite o código do filme da sua sessão: '))
                        sala = int(input('Digite o código da sala : '))
                        data = input('Digite a data da sessão: ')
                        hora = input('Digite o horário da sessão: ')
                        q_ass = int(input('Digite a quantidade de assentos: '))
                        data_hj = date.today()
                        sessao = [filme,sala,data,hora,q_ass,data_hj]
                        lista_sessoes[cod]=sessao
                        print('\nSessão editada com sucesso!\n')
                              
                              
                              
                  else:
                        print('\nSessão não encontrado!')
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
                  #listar filmes cadastrados e seus codigos
                  #gerar codigo automatico
                  #cpf do usuario
                  cod = len(lista_ingressos.keys())+1
                  cpf = int(input('Digite cpf do usuário: '))
                  if cpf in lista_usuarios:
                        for sessao in lista_sessoes:
                             print(f'Código : {sessao}   | Filme : {lista_filmes[lista_sessoes[sessao][0]][0]}')
                        sessao = int(input('\nDigite o código da sessão que deseja comprar ingresso: ')) 
                        valor = float(input('digite o valor do ingresso: '))
                        tipo = input('Digite o tipo do ingresso: ')
                        data_hj = date.today()
                        ingresso = [cpf,sessao,valor,tipo,data_hj]
                        lista_ingressos[cod]=ingresso
                              
                        print('\nIngresso cadastrado com sucesso!\n')
                  else:
                        print("Usuário não cadastrado!Tente novamente")
                        
                  
                  input("Tecle <ENTER> para continuar...")
                        
            elif opcao == 1 :
                  print(
                  """
            Lista de Ingressos 
                  """)
                  print("_"*60)
                  print()
                  for ingresso in lista_ingressos:
                        print(f'''
            Usuário : {lista_ingressos[ingresso][0]}
            Sessão  : {lista_ingressos[ingresso][1]}
            Valor   : {lista_ingressos[ingresso][2]}
            Tipo    : {lista_ingressos[ingresso][3]}
            
                                    ''')
                  input("Tecle <ENTER> para continuar...")
                              
                        
                              
                        
                        
            elif opcao == 2:
                  cod = input('Digite código do ingresso que deseja excluir: ')

                  if lista_ingressos[cod]:
                        lista_ingressos.pop(cod)
                        print('Ingresso excluído!\n')
                        
                  else:
                        print('\nIngresso não encontrado!')
                  input("Tecle <ENTER> para continuar...")
                        
            elif opcao == 3:
                  cod = input('Digite o cod do ingresso que deseja editar: ')
                  if lista_ingressos[cod]:
                        cpf = input('Digite o cpf do usuário:')
                        for sessao in lista_sessoes:
                             print(f'Código : {sessao}   | Filme : {lista_filmes[lista_sessoes[sessao][0]][0]}')
                        sessao = int(input('\nDigite o código da sessão que deseja comprar ingresso: ')) 
                        valor = float(input('digite o valor do ingresso'))
                        tipo = input('Digite o tipo do ingresso: ')
                        data_hj = date.today()
                        ingresso = [cpf,sessao,valor,tipo,data_hj]
                        lista_ingressos[cod]=ingresso
                              
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
            print(f'Total de usuários cadastrados: {len(lista_usuarios)}')
            print('\nUsuários cadastrados hoje:')
            data = date.today()
            cont = 0
            for usuario in lista_usuarios:
                  if lista_usuarios[usuario][3]==data:
                        cont+=1
            print(f'\nUsuários cadastrados hoje: {cont}')
            print()
            primeiro = list(lista_usuarios.keys())[0]
            ultimo = list(lista_usuarios.keys())[-1]
            print(f'''
            Nome  : {lista_usuarios[primeiro][0]}
            CPF   : {primeiro}
            Email : {lista_usuarios[primeiro][1]}
                              ''')
            print("\nÚltimo usuário cadastrado: ")
            print(f'''
            Nome  : {lista_usuarios[ultimo][0]}
            CPF   : {ultimo}
            Email : {lista_usuarios[ultimo][1]}\n
                              ''')
      
      
      elif opcao == 1:
            print()
            print(
            """
      Relátório de Filmes
            """)
            print("_"*60)
            print()
            print(f'Total de filmes cadastrados: {len(lista_filmes.keys())}\n')
            cartaz, ind,acao,drama,com,terror = 0,0,0,0,0,0
            for filme in lista_filmes:
                  if lista_filmes[filme][2]:
                        cartaz +=1
                  else:
                        ind +=1
                  if lista_filmes[filme][1].lower() == 'ação':
                        acao+=1
                  elif lista_filmes[filme][1].lower() == 'drama':
                        drama+=1
                  elif lista_filmes[filme][1].lower() == 'terror':
                        terror+=1
                  elif lista_filmes[filme][1].lower() == 'comédia':
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
            print(f'Total de ingressos cadastrados: {len(lista_ingressos.keys())}\n')
            data = date.today()
            cont=0
            for ingresso in lista_ingressos:
                  if lista_ingressos[ingresso][4] == data:
                        cont+=1
            print(f'Total de ingressos cadastrados hoje:{cont}\n')
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
║ 2 - Módulo de Ingressos                                  ║
║ 3 - Módulo de Relatórios                                 ║
║ 4 - Sobre o Sistema                                      ║
║ 5 - Sair                                                 ║
╚══════════════════════════════════════════════════════════╝
""")
      opcao = int(input('Escolha o módulo que deseja acessar. [0-8] :'))
      print()

      if opcao == 6:
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
      elif opcao==5:
            sessoes()
      else:
            
            print('\nOpção inválida. Tente novamente.\n')
            input("Tecle <ENTER> para continuar...")
      
            
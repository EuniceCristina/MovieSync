import os
from datetime import date
from banco import *

data = str(date.today())
from config import ler_arquivo,escrever_arquivo

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
                  if cpf !="":
                  
                        if cpf in usuarios:
                              print('Cpf já cadastrado. Tente novamente.')
                        else:
                              email = input('Digite um email do usuário: ')
                              valido = False
                              while valido==False:
                                    if '@' in email:
                                          valido = True
                                    else:
                                          print("\nFalha. Digite um email válido.")
                                          email = input('Digite um email do usuário: ')
                              senha = input('Digite uma senha : ')
                              data = str(date.today())
                              pessoa = [nome,email,senha,data]
                              
                              usuarios[f'{cpf}']=pessoa
                              escrever_arquivo('banco/usuarios.txt',usuarios)
                        

                        
                              print('\nUsuário cadastrado com sucesso!\n')
                  else:
                        print('Inválido. Digite um cpf')
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
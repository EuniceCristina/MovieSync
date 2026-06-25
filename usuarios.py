import os
from datetime import date
from banco import *

data = str(date.today())
from config import ler_arquivo,escrever_arquivo, validar_cpf, formatar_cpf, validar_email, definir_status

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
║ 2 - Cancelar Usuário                                     ║
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
                  cpf = formatar_cpf(cpf)
                  validacao_cpf = validar_cpf(cpf)
                  if validacao_cpf:
                  
                        if cpf in usuarios:
                              print('Cpf já cadastrado. Tente novamente.')
                        else:
                              email = input('Digite um email do usuário: ')
                              valido = validar_email(email)
                              
                              senha = input('Digite uma senha : ')
                              data = str(date.today())
                              pessoa = [nome,valido,senha,True,data]
                              
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
                        status = definir_status(usuarios[usuario][3])
                        print(f'''
{list(usuarios.keys()).index(usuario)+1}°

Nome  : {usuarios[usuario][0]}
CPF   : {usuario}
Email : {usuarios[usuario][1]}
Status: {status}
                              ''')
                        print("_"*60)
                  
                  
            
                  
                  input("Tecle <ENTER> para continuar...")
            
            elif opcao == 2:
                  os.system('cls' if os.name == 'nt' else 'clear')
                  print("_"*60)
                  print(
                  """
 Cancelar Usuários 👤
                  """)
                  print("_"*60)
                  usuarios = ler_arquivo('banco/usuarios.txt')
                  cpf = input('\nDigite cpf do usuário que deseja deixar inativo: ')
                  cpf = formatar_cpf(cpf)
                  if cpf in usuarios:
                        usuarios[cpf][3] = False
                        escrever_arquivo('banco/usuarios.txt',usuarios)
                        
                        print('\nUsuário cancelado!\n')
                        
                 
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
                  cpf 
                  usuarios = ler_arquivo('banco/usuarios.txt')
                  if cpf in usuarios:
                        nome = input('Digite o nome do usuario: ')
                        email = input('Digite um email do usuário: ')
                        senha = input('Digite uma senha : ')
                        estado = usuarios[cpf][3]
                        if estado:
                              dis = 'ativo'
                        else:
                              dis = 'inativo'
                        status = input(f'Seu usuário esta {dis}. Deseja mudar status? [S/N] ').upper()
                        if status == 'S':
                              s = not estado
                        
                        nov_usuario = [nome,email,senha,s,usuarios[cpf][4]]
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
import os
from datetime import date
from banco import *

data = str(date.today())
from config import ler_arquivo,escrever_arquivo
from usuarios import usuarios
from filmes import filmes
from salas import salas
from sessoes import sessoes
from ingressos import ingressos
from relatorios import relatorios

#status de salas e ingressos, terminar relatorios


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
      try:
            opcao = int(input('Escolha o módulo que deseja acessar. [0-7] :'))
      
            
            print()

            if opcao == 7:
                  chave = 'N'
                  print('\nAté a próxima.')
                  
            
            elif opcao == 0:
                  
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
                  Versão: 1.0
                  Sistema de Gestão de Cinema
                  Desenvolvido em Python
                  Persistência de dados em arquivos TXT
                  
                  Equipe de desenvolvimento:     
                        Eunice Cristina 
                        @cristinaeunice820@gmail.com
                        
                        
                        
                        """)
                  input("Tecle <ENTER> para continuar...")
            else:
                  
                  print('\nOpção inválida. Tente novamente.\n')
                  input("Tecle <ENTER> para continuar...")
      
      except:
            print('Digite apenas numeros! Tente novamente')
            input("Tecle <ENTER> para continuar...")
            
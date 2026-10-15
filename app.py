import os, colorama, random
from colorama import Fore, Style
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear() #limpar terminal


niveis = [1, 2, 3, 4, 5]
# 0 1 2 3 4 em posição de index


#msg = mensagem, não maddison square garden
msg = ["Nível Muito baixo! (Crítico)", "Nível Baixo", "Nível Médio", "Nível Alto", "Nível Muito Alto!! (Alerta)" ]
# 0 = 1, 1 = 2, 2 = 3, 3 = 4, 4 = 5

def cor_msg(nivel):
    #mensagens dos niveis
        match nivel:
            case 1:
                print(Fore.RED + msg[0] +Style.RESET_ALL)
            case 2:
                print(Fore.YELLOW + msg[1] +Style.RESET_ALL)
            case 3:
                print(Fore.GREEN + msg[2] +Style.RESET_ALL)
            case 4:
                print(Fore.CYAN + msg[3] +Style.RESET_ALL)
            case 5:    
                print(Fore.BLUE + msg[4] +Style.RESET_ALL)
            case _:
                print(Fore.RED + 'Opção inválida.' +Style.RESET_ALL)
            
            
# simulando a exibição para cada nível da lista
print("--- Simulando os níveis do reservatório (os 5 de uma vez)---")
for nivel in niveis:
    #vai rodar os 5 níveis
    print(f"Nível {nivel}: ", end="")
    cor_msg(nivel)
    
# simulação com apenas um nível e aleatoriamente 
print('\n\nSimulação com nível aleatório')
sorteado = random.choice(niveis) #vai escolher entre um dos numeros em níveis e sorteado equivale ao numero sorteado
print(f'Nível {sorteado}:')
cor_msg(sorteado) #chama a função usando o numero sorteado como parametro
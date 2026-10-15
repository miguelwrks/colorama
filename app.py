#O sistema deverá trabalhar com cinco níveis de água, representados em uma lista, indo de um nível mais baixo até o nível máximo do reservatório.  Cada nível deverá ser associado a uma mensagem de alerta e a uma cor, seguindo a progressão de risco:



 #   Utilizar uma lista para armazenar os níveis ou as mensagens do reservatório;
 #   Importar e utilizar a biblioteca colorama;
  #  Criar uma função responsável por definir a cor da mensagem conforme o nível informado;
   # Exibir no terminal a situação atual do reservatório com a cor correspondente;
    #Restaurar o estilo padrão do terminal após a exibição das mensagens.

  #  Não é necessário utilizar entrada de dados do usuário, a simulação pode ser feita com valores definidos no código.

#lvl 1 - muito baixo(critico) - vermelho
#lvl2 baixo - amarelo
#lvl3 medio - verde
#lvl4 - alto - ciano
#lv5 - muito alto (aletra) - azul

import os, colorama
from colorama import Fore, Style


niveis = [1, 2, 3, 4, 5]
# 0 1 2 3 4 em posição de index


#tentar lista das mensagens +ou- assim:
# mensagens =['msg1', 'msg2', etc], ai na hora de colocar a cor puxaria assim: mensagens[0] (posição na lista)

def cor_msg(nivel):
    #mensagens dos niveis
        match nivel:
            case 1:
                print(Fore.RED + "Nível Muito baixo! (Crítico)" +Style.RESET_ALL)
            case 2:
                print(Fore.YELLOW + "Nível Baixo" +Style.RESET_ALL)
            case 3:
                print(Fore.GREEN + "Nível Médio" +Style.RESET_ALL)
            case 4:
                print(Fore.CYAN + "Nível Alto" +Style.RESET_ALL)
            case 5:    
                print(Fore.BLUE + "Nível Muito Alto!! (Alerta)" +Style.RESET_ALL)
            case _:
                print(Fore.RED + 'Opção inválida.' +Style.RESET_ALL)
            
            
# Simulando a exibição para cada nível da lista
print("--- Simulando os níveis do reservatório ---")
for nivel in niveis:
    #vai rodar os 5 níveis
    print(f"Nível {nivel}: ", end="")
    cor_msg(nivel)
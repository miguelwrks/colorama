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

# Inicializa o Colorama (corrige as cores no terminal do Windows)
init(autoreset=True)


niveis = [1, 2, 3, 4, 5]
# 0 1 2 3 4 

print(Fore.RED + "Nível Muito baixo! (Crítico)")
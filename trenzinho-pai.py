import os
import time
import random

# Largura da tela
largura_tela = 80

# Trenzinho em ASCII
trenzinho = [
    "   ~~~~ ____   |~~~~~~~~~~~~~|",
    "  Y_,___|[]|   | Rodrigo ❤️‍🔥!|",
    " {|_|_|_|PU|_,_|_____________|",
    "//oo---OO=OO     OOO     OOO"
]

# Posição inicial do trenzinho
posicao = largura_tela

# Limpa a tela
os.system("cls" if os.name == "nt" else "clear")

while True:
 # Limpa a tela
 os.system("cls" if os.name == "nt" else "clear")

 # Exibe o trenzinho na posição atual
 for linha in trenzinho:
     print(" " * posicao + linha)

 # Atualiza a posição do trenzinho
 posicao -= 1

 # Se o trenzinho ultrapassou a borda da tela, sai do loop
 if posicao < -len(max(trenzinho, key=len)):
    break

 # Aguarda um pouco antes de atualizar a tela novamente
 time.sleep(0.1)

 # Efeito de fumaça
 if random.random() < 0.5:
    print(" " * (posicao + len(trenzinho[0])) + "^")
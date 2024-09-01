import os
import time

# Largura da tela
largura_tela = 80

# Trenzinho em ASCII
trenzinho = "=====_______>"

# Posição inicial do trenzinho
posicao = 0

# Limpa a tela
os.system("cls" if os.name == "nt" else "clear")

while True:
 # Limpa a tela
 os.system("cls" if os.name == "nt" else "clear")

 # Exibe o trenzinho na posição atual
 print(" " * posicao + trenzinho)

 # Atualiza a posição do trenzinho
 posicao += 1

 # Se o trenzinho ultrapassou a borda da tela, sai do loop
 if posicao > largura_tela:
    break

 # Aguarda um pouco antes de atualizar a tela novamente
 time.sleep(0.1)
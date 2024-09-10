#jogo pedra papel e tesoura

import random

print('Bem vindo jogador')
jogador = input("Faca a sua jogada: ").lower()

jogadas = ["pedra", "papel", "tesoura"]
    
maquina = random.choice(jogadas)

if jogador not in jogadas:
    print("escolha invalida, sua jogada sera aleatoria.")
    jogador = random.choice(jogadas)
    print("Sua jogada aleatoria foi:", jogador)

print("o computador jogou:", maquina)

if maquina == jogador:
    print("empate")
elif (jogador == "pedra" and maquina == "tesoura") or\
      (jogador == "papel" and maquina == "pedra") or\
     (jogador == "tesoura" and maquina == "papel"):
    print("Voce ganhou")
else:
    print("Voce perdeu")

import random


def AdivinharNumero():

    maquina = random.randint(1, 10)

    resposta = 3
    jogador = 0

    while (resposta != 0 or jogador != maquina):
        print("Voce tem ", resposta, " palpites")
        jogador = int(input("Digite seu palpite: "))
        resposta -= 1

        if(jogador < maquina):
            print("Maior")
        elif(jogador > maquina):
            print("Menor")
        else:
            print("Parabens voce acertou")
            return

        if resposta == 0:
            print("Seus palpites acabaram, voce perdeu")
            print("A resposta era: ", maquina)

AdivinharNumero()


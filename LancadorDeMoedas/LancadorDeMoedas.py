import random

moeda = ["Cara", "Coroa"]
cara = 0
coroa = 0

jogadas = int(input("Quantos lancamentos deseja fazer? "))

for i in range(jogadas):
    maquina = random.choice(moeda);
    print(maquina)

    if(maquina == "Cara"):
        cara +=1
    else:
        coroa +=1

print("Quantidade de resultados Cara: ", cara, " vezes.")
print("Quantidade de resultados Coroa: ", coroa, " vezes.")
import time
import random
def jogada(jogador):
    if jogador == 0:
        return "pedra"
    elif jogador == 1:
        return "papel"
    elif jogador ==3:
        return"tesoura"

print('Suas opções:')
print("[0] PEDRA")
print("[1] PAPEL")
print("[2] TESOURA")

jogador = int(input("Qual é a sua jogada?"))
computador = random.randint(0,2)

print("JO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PO!!!")
time.sleep(1)

jogador = jogada(jogador)
computador = jogada(computador)

print("-=-"*5)
print("Computador jogou {}".format(computador))
print("Jogador jogou {}".format(jogador))
print("-=-"*5)

if jogador == "pedra" and computador == "tesoura":
    print("Jogador ganhou")
elif jogador == "pedra" and computador =="papel":
    print("Computador ganhou")
elif jogador == "pedra"and computador =="pedra":
    print("Empate")

elif jogador == "papel" and computador == "papel":
    print("Empatou")
elif jogador == "papel" and computador == "pedra":
    print("Jogador ganhou")
elif jogador =='papel' and computador == "tesoura":
    print("Computador ganhou")

elif jogador =="pedra" and computador == "pedra":
    print("Empatou")
elif jogador == "pedra" and computador == "tesoura":
    print("Jogador ganhou")
elif jogador =='pedra' and computador == "papel":
    print("Computador ganhou")



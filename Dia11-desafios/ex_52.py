import random
from time import sleep
print("-=-*20")
print("Sou o seu computador...")
print("Vou pensar num número entre 0 e 10.Tente advinhar...")
print("-=-*20")

chute = int(input("Em que número eu pensei?"))

print("PROCESSANDO...")
sleep(3)
numero = random.randint(0,10)


while(numero != chute):
    chute = int(input("Tente novamente, qual número?"))
else:
    print("Ganhou! O número era {}".format(numero))
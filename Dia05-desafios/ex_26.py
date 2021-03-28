import random
from time import sleep
print("-=-*20")

print("Vou pensar num número entre 0 e 5.Tente advinhar...")

print("-=-*20")

chute = int(input("Em que número eu pensei?"))

print("PROCESSANDO...")
sleep(3)

numero = random.randint(0,5)
if(numero == chute):
    print("Perdi! O número era {}".format(numero))
else:
    print("Ganhei! O número era {}".format(numero))
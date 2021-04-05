from random import randint
print("-="*20)
print("JOGA NA MEGA SENA")
print("-="*20)

jogos= int(input("Quantos jogos você quer que eu faça? "))
lista = []
for i in range(0,jogos):
    for i in range (0,6):
        lista.append(randint(0,60))
    print("{} jogo: {}".format(i,lista))        
    lista.clear()
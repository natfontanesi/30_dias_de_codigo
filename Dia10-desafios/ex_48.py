#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. 
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
lista = []
count_menor=0
count_maior=0

for i in range (0,7):
    lista.append(int(input("Digite o ano de nascimento")))
    if 2021 -lista[i]<=18:
        count_maior+=1
    else:
        count_menor+=1      

print("Ao todo tivemos {} pessoas maiores de idade".format(count_maior))
print("Ao todo tivemos {} pessoas menores de idade".format(count_menor))
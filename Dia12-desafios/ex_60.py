'''Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no 
final do jogo. '''

from random import randint

print("=-"*20)
print("VAMOS JOGAR PAR OU IMPAR")
print("=-"*20)

count = 0
ganhou = True
while ganhou == True:
    num =int(input("Diga um valor: "))
    par_impar= input("Par ou Ímpar [P/I]: ").lower()
    comp_num = randint(0,101)
    soma= num+comp_num

    resultado = ''
    if soma%2==0:
        resultado = 'p'
    else:
        resultado = 'i'

    if resultado == par_impar:
        ganhou = True
        count +=1
        resultado2 = 'PAR'
    else:
        ganhou = False
        resultado2 ='IMPAR'

print("Você jogou {} e o computador {}. Total de {} deu {}".format(num,comp_num,soma,resultado2))
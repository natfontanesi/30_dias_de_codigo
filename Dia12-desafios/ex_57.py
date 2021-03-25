'''Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
 No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''
num = int(input("Digite um número ou [999] para parar"))
lista = []

while(num!=999):
    lista.append(num)
    num = int(input("Digite um número ou [999] para parar"))

print("Você digitou {} números, e a soma deles é {} ".format(len(lista),sum(lista)))
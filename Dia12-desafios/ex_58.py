'''Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

num = int(input("Digite um número"))
cont = input("Deseja continuar? S/N").lower()
lista = [num]

while(cont!='n'):
    num = int(input("Digite um número"))
    lista.append(num)
    cont = input("Deseja continuar? S/N").lower()

media = sum(lista)/len(lista)
print("O maior número digitado foi {}, o menor número digitado foi {}, e a média é {}".format(max(lista), min(lista),media))
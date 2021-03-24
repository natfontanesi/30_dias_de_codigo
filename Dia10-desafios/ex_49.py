'''Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final,
mostre qual foi o maior e o menor peso lidos.'''
lista=[]
for i in range (0,5):
   lista.append(float(input("Digite o peso: "))) 
   
print("O menor peso lido foi {}".format(min(lista)))

print("O menor peso lido foi {}".format(max(lista)))
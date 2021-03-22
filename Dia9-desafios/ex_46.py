#Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input("Digite um número: "))
count=0

for i in range(1,num+1):
    if num % i ==0:
        print('\033[33m',end='')
        count+=1
    else:
        print('\033[31m', end='')
    print('{}'.format(i), end=' ')

print("\nO número {} foi divisível {} vezes".format(num,count))

if(count<3):
    print("É PRIMO")
else:
    print("NÃO É PRIMO")
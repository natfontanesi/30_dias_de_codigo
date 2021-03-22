'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
 Se o valor digitado for ímpar, desconsidere-o.'''

lista = []

for i in range (0,6):
    lista.append(int(input("Digite um número")))

for i in lista:
    if(i%2 != 0):
        lista.remove(i)
    

    
print("Foram {} números pares, a soma é {}".format(len(lista),sum(lista)))

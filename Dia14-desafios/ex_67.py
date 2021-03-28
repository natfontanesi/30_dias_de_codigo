'''Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e 
cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). 
No final, mostre a lista ordenada na tela.'''

lista =[]
for i in range(0,5):
    num = int(input("Digite um valor"))
    if i == 0:
        lista.append(num)
    elif num>lista[len(lista)-1]:
        lista.append(num)
    else:
        pos = 0
        while pos<len(lista):
            if num<=lista[pos]:
                lista.insert(pos,num)
                break
            pos+=1
            
print("Os valores digitados em ordem {}".format(lista))
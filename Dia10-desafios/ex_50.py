'''Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e 
quantas mulheres tem menos de 20 anos.'''
lista_nome=[] 
lista_idade=[]
lista_sexo = list()
count_mulheres =0
indice_homem =0
idade_homem = 0
media=0


for i in range (0,4):
    print("{}ª pessoa".format(i+1))
    lista_nome.append(input("Nome: "))
    lista_idade.append(int(input("Idade")))
    lista_sexo.append(input("Sexo M/F: ").lower())
    if lista_sexo[i]=='m' and lista_idade[i]>idade_homem:
        idade_homem=lista_idade[i]
        indice_homem=i
    if lista_sexo[i] == 'f' and lista_idade[i]<20:
        count_mulheres +=1
    
    
media = sum(lista_idade)/4

print("A média de idade do grupo é {}".format(media))
print("O homem mais velho tem {} anos e se chama {}".format(idade_homem,lista_nome[i]))
print("Ao todo são {} mulheres com menos de 20 anos".format(count_mulheres))

    
    
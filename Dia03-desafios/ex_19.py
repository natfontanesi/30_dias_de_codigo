from random import shuffle
lista = []

lista.append(input("Nome do primeiro aluno: "))
lista.append(input("Nome do segundo aluno: "))
lista.append(input("Nome do terceiro aluno: "))
lista.append(input("Nome do quarto aluno: "))

shuffle(lista)

print("A ordem de apresentação é: ")
print(lista)

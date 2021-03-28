import random
lista = []

lista.append(input("Nome do primeiro aluno: "))
lista.append(input("Nome do segundo aluno: "))
lista.append(input("Nome do terceiro aluno: "))
lista.append(input("Nome do quarto aluno: "))

num = random.choice(lista)

print("O aluno escolhido foi {}".format(num))
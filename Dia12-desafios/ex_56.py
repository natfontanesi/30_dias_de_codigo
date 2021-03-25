num = int(input("Quantos números vc quer mostrar?"))

lista= [0,1]

for i in range(2,num):
    soma = lista[i-1]+lista[i-2]
    lista.append(soma)

print(lista)
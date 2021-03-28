num1 = int(input("Digite um número"))
num2 = int(input("Digite outro número"))
num3 = int(input("Digite mais um número"))
num4 = int(input("Digite o último número"))
count = 0
tupla = (num1,num2,num3,num4)

print('O valor 9 apareceu {} vezes'.format(tupla.count(9)))

print("O valor 3 apareceu na {} posição".format(tupla.index(3)))

for i in tupla:
    if i % 2==0:
        count +=1
print("foram digitados {} números pares".format(count))
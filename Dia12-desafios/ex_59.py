
num = int(input("Digite um número para ver sua tabuada: "))
while num > 0 :
    for i in range (1,11):
        print("{} x {} = {}".format(num,i,num*i))
    num = int(input("Digite um número para ver sua tabuada: "))

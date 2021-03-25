print("="*15)
print("10 TERMOS DE UMA PA")
print("="*15)
termo1 = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo= termo1+(10-1)*razao
count = 1

while count <=10:
    print("{}".format(termo1), end= ' -> ')
    termo1 += razao
    count +=1
print("ACABOU")
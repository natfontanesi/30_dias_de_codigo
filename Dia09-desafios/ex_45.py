print("="*15)
print("10 TERMOS DE UMA PA")
print("="*15)
termo1 = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo= termo1+(10-1)*razao

for i in range(termo1,decimo,razao):
    print("{}".format(i), end= ' -> ')
print("ACABOU")
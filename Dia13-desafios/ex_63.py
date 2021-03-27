print("="*20)
print("BANCO CEV")
print("="*20)

valor= int(input("Que valor você quer sacar?"))
ced_50 = 0
ced_10 = 0
ced_1 = 0
if valor>50:
    ced_50 = int(valor/50)
    ced_10 = int((valor% 50) /10)
    ced_1 = int(((valor% 50) %10))
elif valor<50:
    ced_10= int(valor/10)
    ced_1 = int((valor %10))
else:
    ced_1 =int( valor /1)

print("Total de {} cédulas de 50".format(ced_50))
print("Total de {} cédulas de 10".format(ced_10))
print("Total de {} cédulas de 01".format(ced_1))
import time
num = int(input("Digite um número para contar: "))

for i in range (num,-1,-1):
    print(i)
    time.sleep(1)

print("Acabou")


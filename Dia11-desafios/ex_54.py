from math import factorial
num = int(input("Digite um número para calcular seu fatorial: "))

resultado = factorial(num)
print("Calculando {}! = ".format(num), end='')

for i in range (num, 1,-1):
    print("{} x ".format(i),end='')
    
print("= {}".format(resultado))
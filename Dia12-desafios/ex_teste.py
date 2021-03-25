from random import randint

print("=-"*20)
print("VAMOS JOGAR PAR OU IMPAR")
print("=-"*20)

count = 0
ganhou = True

while ganhou == True:
    num =int(input("Diga um valor: "))
    par_impar= input("Par ou Ímpar [P/I]: ").lower()
    comp_num = randint(0,101)
    soma= num+comp_num
    
    resultado = ''
    if soma%2==0:
        resultado = 'p'
    else:
        resultado = 'i'

    if resultado == par_impar:
        ganhou = True
        count +=1
    else:
        ganhou = False

lista = []
pares=[]
impares = []
opcao = 's'
while opcao == 's':
    num = int(input("Digite um valor: "))
    if num not in lista:
        lista.append(num)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado! Não vou adicionar")
        
    opcao = input("Deseja continuar? [S/N]: ").lower()  
    
for i in lista:
    if i % 2 ==0:
        pares.append(i)
    else:
        impares.append(i)

print("A lista foi: {}".format(lista))
print("Os números pares são: {}".format(pares))
print("Os números ímpares são: {}".format(impares))
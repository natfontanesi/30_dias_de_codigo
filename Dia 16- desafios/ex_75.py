lista = []
lista_par = []
lista_impar=[]
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
        if i % 2 == 0:
            lista_par.append(i)
        else:
            lista_impar.append(i)  
            
print(lista_par.sort())
print(lista_impar.sort())
lista = []
opcao = 's'
while opcao == 's':
    num = int(input("Digite um valor: "))
    if num not in lista:
        lista.append(num)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado! Não vou adicionar")
        
    opcao = input("Deseja continuar? [S/N]: ").lower()      

print("Você digitou {} elementos".format(len(lista)))

lista.sort(reverse=True)
print("A lista em ordem decrescente é {}".format(lista)) 

if 5 in lista:
    eh_lista = "faz"
else:
    eh_lista="não faz"

print( "O valor 5 {} parte da lista".format(eh_lista)) 
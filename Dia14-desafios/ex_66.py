'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente. '''
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

print("Você digitou os valores {}".format(lista.sort))
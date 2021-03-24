'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''


def menu():
    print("[ 1 ] somar")
    print("[ 2 ] multiplicar")
    print("[ 3 ] maior")
    print("[ 4 ] novos números")
    print("[ 5 ] sair do programa")
    opcao= int(input("Qual é a sua opção>>>>>> "))
    while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5:
        opcao= int(input("Opção inválida. Qual é a sua opção>>>>>> "))

    return opcao

num1= int(input("Primeiro Valor: "))
num2= int(input("Segundo Valor: "))
opcao = menu()


if opcao==1:
    print(num1+num2)
elif opcao ==2:
    print(num1+num2)
elif opcao == 3:
    if num1>num2:
        print(num1)
    else:
        print(num2)
elif opcao==4:
    opcao = menu()
elif opcao == 5:
    print('Finalizando...')
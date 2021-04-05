matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma_pares=0
soma_3 = 0

for linha in range (0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input("Digite um valor para {} e {}: ".format(linha, coluna)))
        
for linha in range (0,3):
    for coluna in range(0,3):
        print(f'{matriz[linha][coluna]}',end='')
    print()
    
maior = matriz [1][0]
for linha in range (0,3):
    for coluna in range(0,3):
        if matriz [linha][coluna]%2 == 0:
            soma_pares+= matriz [linha][coluna]
        if coluna == 2:
            soma_3+= matriz [linha][coluna]
        if linha == 1:
            if maior < matriz [linha][coluna]:
                maior = matriz [linha][coluna]
print("A soma dos numeros pares é {}".format(soma_pares)) 
print("A soma da terceira coluna é {}".format(soma_3))
print("O maior valor da segnda linha é {}".format(maior))        

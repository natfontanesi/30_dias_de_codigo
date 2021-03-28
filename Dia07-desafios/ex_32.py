num = int(input("Digite um número inteiro: "))

print("Escolha uma das bases para conversão:")
print("[1] converter para BINÁRIO")
print("[2] converter para OCTAL")
print("[3] converter para HEXADECIMAL")

opcao = int(input("Sua opção: "))
resultado = 0

if opcao == 1:
    resultado = bin(num)
elif opcao == 2:
    resultado = oct(num)
elif opcao == 3:
    resultado = hex(num)
else:
    opcao = int(input("Sua opção: "))

print("A conversão escolhida foi {}. O resultado é: {}".format(opcao,resultado))
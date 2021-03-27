numeros = ('zero', 'um', 'dois', 'três','quatro', 'cinco', 'seis', 'sete', 'oito','nove','dez', 'onze', 'doze', 'treze', 'quatorze','quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = 0
while num >=0 and num <=20:
    num = int(input("Digite um número entre 0 e 20: "))
    break
else:
    print("Tente novamente!")
    num = int(input("Digite um número entre 0 e 20: "))

print("Você digitou o número {}".format(numeros[num]))
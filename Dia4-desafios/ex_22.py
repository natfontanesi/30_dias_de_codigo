numero = int(input("Digite um número"))
unidade= numero % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10 
milhar = numero // 1000 % 10
print("Unidade: {}".format(unidade))
print("Dezena: {}".format(dezena))
print("Centena: {}".format(centena))
print("Milhar: {}".format(milhar))
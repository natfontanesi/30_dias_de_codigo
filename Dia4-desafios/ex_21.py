nome = input("Digite seu nome completo: ")
print("Analisando seu nome...")

nome2= nome.replace(" ",'')
nome3 = nome.split(" ")

print("Seu nome em maiusculas é {}".format(nome.upper()))
print("Seu nome em maiusculas é {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras". format(len(nome2)))
print("Seu primeiro nome é {} e ele tem {} letras".format(nome3[0], len(nome3[0])))
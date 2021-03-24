sexo = input("Informe seu sexo M/F: ").lower()
while sexo != 'm' and sexo != 'f':
    sexo = input("Dados inválidos. Informe seu sexo M/F: ").lower()
print("Sexo {} registrado".format(sexo))
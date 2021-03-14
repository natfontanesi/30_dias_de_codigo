frase = input("Digite algo: ")
print('O tipo primitivo é:',type(frase))

print('Só tem espaços?',frase.isspace())

print('Só tem números?',frase.isnumeric())

print('é alfabético?',frase.isalpha())

print("É alfanumerico",frase.isalnum())

print("É tudo maiuscula",frase.isupper())

print("É tudo minuscula",frase.islower())

print("Está capitalizada", frase.istitle())





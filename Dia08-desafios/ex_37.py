peso = float(input("Qual é o seu peso?"))
altura = float(input("Qual é o sua altura?"))
imc = peso / (altura**2)

print("O IMC dessa pessoa é de {:.2f}".format(imc))

if imc<18.5:
    print('Está abaixo do peso')
elif imc >=18.5 and imc < 25:
    print('Está no peso ideal')
elif imc>=25 and imc < 30:
    print('Está com sobrepeso')
elif imc>= 30 and imc <= 40:
    print('Está com obesidade')
else: 
    print('Está com obesidade mórbida')
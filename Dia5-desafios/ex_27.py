velocidade = int(input("Qual é a velocidade atual do carro"))
multa = ((velocidade-80)*7)
if(velocidade<=80):
    print("Tenha um bom dia! Dirija com segurança")


elif(velocidade>80):
    print("MULTADO!  Você excedeu o limite permitido de 80km/h, multa de: R${:.2f}".format(multa))
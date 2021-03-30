lista_peso=[]
lista_nomes=[]

continua= 's'
while continua =='s':
    lista_nomes.append(input("Digite o nome: "))
    lista_peso.append(float(input("Digite o peso: ")))
    continua = input("Deseja continuar? S/N ").lower()
    
print("Foram cadastradas {} pessoas".format(len(lista_nomes)))
maior = lista_peso[0]
menor = lista_peso[0]
indice_maior = 0
indice_menor=0
for i in range(0,len(lista_nomes)):
    if maior < lista_peso[i]:
        maior = lista_peso[i]
        indice_maior = i
    if menor> lista_peso[i]:
        menor = lista_peso[i]
        indice_menor = i
print("O menor peso é {} de {}".format(menor,lista_nomes[indice_menor]))
print("O maior peso é {} de {}".format(maior,lista_nomes[indice_maior]))
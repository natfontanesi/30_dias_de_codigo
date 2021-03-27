lista_sexo =[]
lista_idade=[]
continuar = 's'

count_18 = 0
count_h = 0
count_m_20 =0

while continuar == 's':
    print("-"*20)
    print("CADASTRE UMA PESSOA")
    print("-"*20)
    lista_idade.append(int(input("Idade: ")))
    lista_sexo.append(input("Sexo M/F: ").lower())
    
    print("-"*20)
    continuar = input("Quer continuar? S/N ").lower()


for i in range(0,len(lista_idade)):
    if(lista_idade[i]>18):
        count_18 += 1
    elif(lista_idade[i]<20):
        if lista_sexo[i]== 'f':
            count_m_20 +=1
    elif (lista_sexo[i]=='m'):
        count_h +=1

print("Total de pessoas com mais de 18 anos: {}".format(count_18))
print("Ao todo temos {} homens cadastrados".format(count_h))
print("E temos {} mulheres com menos de 20 anos".format(count_m_20))
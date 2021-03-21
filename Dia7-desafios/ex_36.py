ano = int(input("Ano de Nascimento"))
idade = 2021-ano
print("O atleta tem {} anos".format(idade))
classificacao = ""

if idade<=9:
    classificacao="MIRIM"
elif idade>9 and idade<=14:
    classificacao="INFANTIL"
elif idade>14 and idade<=19:
    classificacao="JÚNIOR"
elif idade>19 and idade <=25:
    classificacao = "SÊNIOR"
else:
    classificacao= "MASTER"

print("Classificação {}".format(classificacao))
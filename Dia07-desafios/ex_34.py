ano = int(input("Ano de Nascimento: "))

atual = 2021
ano_alistamento= ano+18
idade= atual-ano
anos_faltantes = 18-idade

print("Quem nasceu em {} tem {} anos em {}.".format(ano,idade,atual))
if idade< 18:
    print("Ainda faltam {} anos para o alistamento".format(anos_faltantes))
print("Seu alistamento será em {}".format(ano_alistamento))
from datetime import datetime

dados_func = {}
dados_func['nome']= input("Nome:")
nasc= int(input("Ano de nascimento"))
dados_func ["idade"] = datetime.now().year - nasc
dados_func["CTPS"]= int(input*"Carteira de Trabalho (0) nao tem: ")
if dados_func["Ctps"]!= 0 :
    dados_func["contratação"] = int(input("Ano de Contratação: "))
    dados_func["salario"]=float(input("Salário R$: "))
    dados_func["Aposentadoria"]= ((dados_func["contratação"]+35)-datetime.now().year)
    print(dados_func)
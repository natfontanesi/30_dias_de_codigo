from io import open_code


print("======LOJAS GUANABARA======")

preco = float(input("Preço das compras: R$"))

print("FORMAS DE PAGAMENTO")
print("[1] à vista dinheiro/cheque")
print("[2] à vista cartão")
print("[3] 2x no cartão")
print("[4] 3x no cartão")

opcao = int(input('Qual é a opção: '))
parcelas = int(input('Quantas parcelas: '))
juros=""
valor= 0
parcela = 0 

if opcao == 1:
    valor = preco * 0.90
    parcela = valor
    juros= "Sem juros"

elif opcao == 2:
    valor = preco * 0.95
    parcela = valor
    juros= "Sem juros"

elif opcao == 3:
    valor = preco
    parcela = valor/parcelas
    juros= "Sem juros"

elif opcao ==4:
    valor = preco * 1.2 
    parcela = valor/parcelas
    juros= "Com juros"
    
print("Sua compraserá parcelada em {}x deR${} {}".format(parcelas,parcela,juros))

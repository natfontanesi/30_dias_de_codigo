continuar = 's'
lista_produto = []
lista_preço = []

count_prod = 0
prod_barato = ""
print('-'*20)
print("LOJA SUPER BARATÃO")
print('-'*20)

while continuar == 's':
    lista_produto.append(input("Nome do Produto: ").lower())
    lista_preço.append(float(input("Preço: ")))
    continuar = input("Quer continuar? [S/N] ")

prod_barato = min(lista_preço)
for i in range(0,len(lista_preço)):
    if lista_preço[i]>1000:
        count_prod +=1
    elif lista_preço[i] == prod_barato:
        prod_barato = i



print('-'*20)
print("FIM DO PROGRAMA")
print('-'*20)
print("O total da compra foi {}".format(sum(lista_preço)))
print("Temos {} produtos que custam mais de mil reais".format(count_prod))
print("O produto mais barato foi {} que custa {}".format(lista_produto[prod_barato],lista_preço[prod_barato]))

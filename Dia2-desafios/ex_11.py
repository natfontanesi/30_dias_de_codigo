produto = float(input("Qual o preço do produto? "))

produto_desconto = produto*0.95

print("O produto que custava R${}, na promoção com desconto de 5% custará R${:.2f}.".format(produto,produto_desconto))
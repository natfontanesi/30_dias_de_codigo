dias = int(input("Quantos dias alugado? "))
km = float(input("Quantos Km rodados?"))

total = dias * 60 + km * 0.15

print("O total a pagar é de R${:.2f}".format(total))
cateto_oposto = float(input("Comprimento do cateto oposto: "))
cateto_adjacente = float(input("Comprimento do cateto adjacente: "))

hipotenusa = (cateto_adjacente**2 + cateto_oposto**2)**0.5

print("A hipotenusa vai medir {:.2f}".format(hipotenusa))
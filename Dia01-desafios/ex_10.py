largura=float(input("Largura da parede: "))
altura= float(input("Altura da parede: "))

area= largura*altura
tinta = area/2

print("Sua parede tem a dimensão de {}X{} e sua área é de {}m²".format(altura,largura,area))
print("Para pintar essa parede vc precisa de {}l de tinta".format(tinta))
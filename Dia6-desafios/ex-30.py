print(-=-*20)
print("Analisador de Triangulos")
print(-=-*20)

primeiro= float(input("Primeiro Segmento: "))
segundo= float(input("Segundo Segmento: "))
terceiro= float(input("Terceiro Segmento: "))

if primeiro< segundo + terceiro and segundo< primeiro + terceiro and terceiro< primeiro+segundo:
    print("Os segmentos podem formar um triangulo!")

else:
    print("Os segmentos não podem formar um triangulo!")
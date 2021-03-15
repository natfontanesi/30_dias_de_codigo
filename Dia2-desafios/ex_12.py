salario = float(input("Qual o salário do funcionário? "))

salario_reajustado = salario*1.15

print("Um funcionário que ganhava R${:.2f}, com 15% de aumento passa a ganhar R${:.2f}".format(salario,salario_reajustado))
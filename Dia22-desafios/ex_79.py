ficha = []
while True:
    nome=input("Nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1+nota2)/2
    ficha.append([nome, [nota1,nota2],media])
    resposta = input("Quer continuar? S/N: ")
    if resposta in "nN":
        break
print("-="*30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print("--"*30)
for i, a in enumerate(ficha):
    print(f'({i:<4}{a[0]:<10}{a[2]:>8.1f})')
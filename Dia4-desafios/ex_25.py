frase = input("Digite uma frase:").lower()

frase.strip()

print("A letra a aparece {} vezes".format(frase.count('a')))
print("A primeira ocorrencia da letra a é na {} posição".format(frase.find('a')+1))
print("A ultima ocorrencia da letra a é na {} posição".format(frase.rfind('a')+1))


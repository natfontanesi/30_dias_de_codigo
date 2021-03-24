'''Exercício Python 053: Crie um programa que leia uma frase qualquer e
diga se ela é um palíndromo, desconsiderando os espaços.'''

frase = input("Digite uma frase: ").strip().lower()

palavras=frase.split()
junto = ''.join(palavras)
frase_inversa = ''

frase_inversa = junto[::-1]

if(junto == frase_inversa):
    print("Temos um palíndromo!")
else:
    print("Não temos um palíndromo")
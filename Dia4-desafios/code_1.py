def is_isogram(string):
    lista=[]
    for letra in string:
        if letra.isalpha():
            lista.append(letra.lower())
    if len(lista)== len(set(lista)):
        return True
    else:
        return False
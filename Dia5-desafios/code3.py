def alphabet_position(text):
    saida = '' 
    for letra in text.lower(): 
        if letra.isalpha(): 
            saida = saida + str(ord(letra) - 96) + ' ' #find its value, taken from stackoverlfow
    saida = saida.strip() 
    return saida 
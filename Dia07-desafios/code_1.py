'''Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's 
divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string 
'(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).'''
def divisors(integer):
    cont=0
    lista = []
    retorna= ""
    for i in range (2, integer):
        if integer%i==0:
            cont +=1
            lista.append(i)
    if cont <=0:
        retorna = "{} is prime".format(integer)
        return retorna
    else:
        return lista
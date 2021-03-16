def get_sum(a,b):
    soma=0
    if a>b:
        for i in range(b,a+1):
            soma+=i
    elif a<b:
        for i in range(a,b+1):
            soma+=i
    else:
        return a
    return soma
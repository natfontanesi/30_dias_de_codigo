def odd_or_even(arr):
    soma=0
    for num in arr:
        soma+=num
    if(soma%2==0):
        return "even"
    else:
        return "odd"
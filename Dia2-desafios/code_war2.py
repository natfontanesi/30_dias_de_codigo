def sum_square_even_root_odd(nums):
    list=[]
    for num in nums:
        if num%2==0:
            list.append(num**2)
        else:
            list.append(num**0.5)
    
            
    return round(sum(list),2)
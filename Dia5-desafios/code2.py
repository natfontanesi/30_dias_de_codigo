def tickets(people):
    troco = 'YES'
    vinte, cinquenta, cem = 0, 0, 0
    
    for dinheiro in people:
        if troco == 'NO':
            break

        if dinheiro == 25:
            vinte += 1

        elif dinheiro == 50 and vinte > 0:
            vinte -= 1
            cinquenta += 1

        elif dinheiro == 100:
            if cinquenta > 0 and vinte > 0:
                cinquenta -= 1
                vinte -= 1
                cem += 1
                
            elif vinte > 2:
                vinte -= 3
                cem += 1
            else:
                troco = 'NO'
        else:
            troco = 'NO'
            
    return troco
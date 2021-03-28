pilha1 = []
pilha2 = []
for i in range(0,len(texto)):
    if i== 0 and texto[i]==")":
        return False
    if texto[i] == '(':
        pilha1.append(texto[i])
    elif texto[i] == ')':
        pilha2.append(texto[i])
        
    if len(pilha1)==len(pilha2):
      return True
    
    else:
      return False
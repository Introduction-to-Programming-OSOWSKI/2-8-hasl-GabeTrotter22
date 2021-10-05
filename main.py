def hasL(w):
    
    x = 0
    
    while x < len(w):
        if w[x] == "l":
            return True
             
        x = x + 1
    return False

        

print(hasL("length"))
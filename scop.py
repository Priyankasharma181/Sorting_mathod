def recursive(a):
    if a == 1:
        return 1
    return a*(recursive(a-1))    
print(recursive(3))    

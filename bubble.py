# bubble short
i = [2,7,1,9]
def b(a):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]= a[j+1],a[j]
    return a
print(b(i))
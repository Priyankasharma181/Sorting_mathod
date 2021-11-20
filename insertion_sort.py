a = [3,5,6,3,2,4]
def inserton(b):
    for i in range(len(b)):
        c = a[i]
        j = i-1
        while c<a[j]:
            a[j+1] = a[j]
            a[j] = c
            i-=1
            
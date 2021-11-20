# select shorting
list1= [8,3,5,2,5,7]

def select(a):
    for i in range(len(a)):
        c = i
        for j in range(len(a)):
            if a[c]<a[j]:
                a[j],a[c] = a[c],a[j]
    return a
print(select(list1))

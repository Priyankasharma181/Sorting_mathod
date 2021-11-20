#  quick shorting

list1 = [8,2,3,5,2,7,8,9]
def quicksort(l):
    if len(l)<=1:
        return l
    else:
        pivot = l.pop()
    greater = []
    lower = []
    for i in l:
        if i > pivot:
            greater.append(i)
        else:
            lower.append(i)
    return quicksort(lower)+[pivot]+quicksort(greater)   
print(quicksort(list1))  

a = [3,5,2,6,6]
def avarage(list_1):
    sum = 0
    i = 0
    while i<len(list_1):
        sum = sum+list_1[i]
        i+=1
    avgare_of_list = sum/len(list_1)
    return avgare_of_list

print(avarage(a))             
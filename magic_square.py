magic_square = [[8, 3, 4],
                [1, 5, 9],
                [6, 7, 9]]
sum = 0
for i in range(len(magic_square)):
    for j in range(len(magic_square[i])):
        if i==j:
            sum=sum+magic_square[i][j]    
print(sum)
sum_1 = 0
for k in range(len(magic_square)) :
    for l in range(len(magic_square[k])):
        if k+l==len(magic_square[k])-1:
            sum_1=sum_1+magic_square[k][l]    
print(sum_1) 
c1sum = 0
c2sum = 0
c3sum = 0
for m in range(len(magic_square)):
    for n in range(len(magic_square[m])):
        if n==0:
            c1sum = c1sum + magic_square[m][n]
        elif n==1:
            c2sum = c2sum + magic_square[m][n]
        elif n==2:
            c3sum = c3sum + magic_square[m][n]
print(c1sum , c2sum , c3sum) 
r1sum = 0
r2sum = 0
r3sum = 0
for p in range(len(magic_square)):
    for q in range(len(magic_square[p])):
        if p == 0:
            r1sum = r1sum + magic_square[p][q]
        elif p == 1:
            r2sum = r2sum + magic_square[p][q]
        elif p == 2:
            r3sum = r3sum + magic_square[p][q]
print(r1sum , r2sum , r3sum)  
if r1sum == r2sum ==r3sum ==c1sum==c2sum==c3sum==sum==sum_1:
    print("it is magic square")
else:
    print("it is not magic square")                       


                                 
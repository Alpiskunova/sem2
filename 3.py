A = list(map(int, input().split()))
b= len(A)
c=1
for i in range(len(A)):
    c=c*A[i]


print((c*A[i])**(1/b))
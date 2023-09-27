#task 4
A = list(map(int, input().split()))

for i in range(0,len(A)//2):
    A[i*2], A[i*2+1] = A[i*2+1], A[i*2]
print(A)

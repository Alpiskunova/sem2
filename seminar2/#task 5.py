#task 5 
A = list(map(int, input().split()))
for i in range(1, len(A)):
    A[-i], A[-(i+1)] = A[-(i+1)], A[-i]
print(A)
#1

def fib(N, fibs):
    if N== 1:
        fibs[0] = 0
        return fibs[0]
    if N== 2:
        fibs[1] = 1
        return fibs[1]
    
    if fibs[N-1] != 0:
        return fibs[N-1]

    fibs[N-1] = fib(N - 1, fibs) + fib(N - 2, fibs)
    print(fibs)
    return fibs[N-1]

N= 10
fibs= [0 for i in range(N)]
print(fib(N, fibs))

N= int(input())
fibs= [0 for i in range(N)]

fibs[0]= 0
fibs[1]= 1

for i in range(2,N):
    fibs[i]= fibs[i-1] + fibs[i-2]

print(fibs)

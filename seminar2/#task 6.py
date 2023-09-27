#task 6
a= [int(b) for b in input().split()]
for m in range(len(a)):
    for n in range(len(a)):
        if m != n and a[m]==a[n]:
            break
    else:
        print(a[m], end=' ')
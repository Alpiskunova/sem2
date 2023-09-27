#task 1
a = list(map(int, input().split()))
print(a[0] * (a[0] + 1) // 2 - sum(a[1:]))
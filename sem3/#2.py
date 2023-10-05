#2

n = int(input())
list = []
a= 2
while n> 1:
    if n%a == 0:
        list.append(a)
        n= n/a
    else:
        a += 1
print(list)
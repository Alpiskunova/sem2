#task 7
a= list(map(int, input().split()))
b= a[0]
c= a.count(b)
for i in a:
     if a.count(elem) > c:
          b= elem
          c= a.count(elem)
print(b)
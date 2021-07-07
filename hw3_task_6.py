a = []
n = int(input())
x = 0
y = 0
from random import randint as r
for i in range(n):
    a.append(r(1,50))
    if a[i]>a[i-1] :
       x +=1
print(a)
print(x)
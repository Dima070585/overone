a = []
n = int(input())
s = 0
sr = 0
sum = 0
from random import randint as r
for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(int(r(1,30)))
for i in a:
    print(i)
for i in range(n):
    m = max(a[i])
    print(m)
for i in range(n):
    a[i][i],m = m,a[i][i]



for i in a:
    print(i)
print(m)
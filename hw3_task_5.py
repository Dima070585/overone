a = []
from random import randint as r
for i in range(19):
    a.append(r(1,30))
m = max(a)
print(a)
for i in range(19):
    if a[i]%2 == 0:
        a[i]=m
print(a)
print(m)


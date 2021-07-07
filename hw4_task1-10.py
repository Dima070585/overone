x = []
a = int(input())
b = int(input())
n = int(input())
m = int(input())
maks = []
s = 0
from random import randint as r
for i in range(n):
    x.append([])
    for j in range(m):
        x[i].append(int(r(a,b)))
print(x)

for i in x:
    print(i)
for k in x:
    for j in k:
        maks.append(j)
        s = s+j
print("max =",max(maks))
print("min= ",min(maks))
print("sum= ",s)
max_sum = 0
col = 0
for i in range(n):
    s = 0
    for j in range(m):
        s += x[i][j]
    print("%3d" % s, end='')
    if s > max_sum:
        max_sum = s
        col = i
print()
print("индекс максимального ряда:",col+1)
min_sum = 100
col = 0
for i in range(n):
    s = 0
    for j in range(m):
        s += x[j][i]
    print("%3d" % s, end='')
    if s < min_sum:
        min_sum = s
        col = i
print()
print("индекс минимальной колонки:",col+1)
min_sum = 100
col = 0
for i in range(n):
    s = 0
    for j in range(m):
        s += x[i][j]
    print("%3d" % s, end='')
    if s < min_sum:
        max_sum = s
        col = i
print()
print("индекс минимального ряда:",col+1)
max_sum = 100
col = 0
for i in range(n):
    s = 0
    for j in range(m):
        s += x[j][i]
    print("%3d" % s, end='')
    if s > max_sum:
        min_sum = s
        col = i
print()
print("индекс максимальной колонки:",col+1)
for i in range(n):
    for j in range(i+1,n):
        x[i][j]=0
for i in x:
    print(i)
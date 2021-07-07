a = 'kjuyf mnfkfff'
e=0
for i,elem in enumerate(a):
    if elem == 'f':
        e += 1
        if e == 2:
            print(i)
if e == 1:
    print(-1)
elif e == 0:
    print(-2)

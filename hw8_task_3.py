n = int(input('введите число от 1 до 9: '))
a = []
for i in range(1,n+1):
    a.append(i)
    b = ''.join(str(e) for e in a)
    print(b)
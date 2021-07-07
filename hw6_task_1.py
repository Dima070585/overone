def fact2(n):
    if n > 0:
        if n%2 != 0:
            a = 1
            while n > 1:
                a *= n
                n -= 2
        if n%2 == 0:
            a = 1
            while n > 1:
                a *= n
                n -= 2
    else:
        a ='error'
    return (a)
print(fact2(6))

n = int(input())

a=1
for i in range(1,n+1):
    a *= i

    print(a)
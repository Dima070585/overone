def num(a,b,c):
    if a == b and b == c:
        print(3)
    elif a == b or b == c or a == c:
        print(2)
    else:
        print(0)
num(15,15,15)
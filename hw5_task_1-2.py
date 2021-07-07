
def func_1(a):
    rez = a * 2.54
    return rez
def func_2(a):
    rez = a * 0.393701
    return rez
def func_3(a):
    rez = a * 1.60934
    return rez
def func_4(a):
    rez = a * 0.621371
    return rez
def func_5(a):
    rez = a * 0.453592
    return rez
def func_6(a):
    rez = a * 2.20462
    return rez
def func_7(a):
    rez = a * 28.3495
    return rez
def func_8(a):
    rez = a * 0.035274
    return rez
def func_9(a):
    rez = a * 3.78541
    return rez
def func_10(a):
    rez = a * 0.264172
    return rez
def func_11(a):
    rez = a * 0.473176
    return rez
def func_12(a):
    rez = a * 2.11338
    return rez
while True:
    b = int(input("введите число от 1 до 12: "))
    if b == 1:
        a = float(input("a= "))
        print(func_1(a))
    elif b == 2:
        a = float(input("a= "))
        print(func_2(a))
    elif b == 3:
        a = float(input("a= "))
        print(func_3(a))
    elif b == 4:
        a = float(input("a= "))
        print(func_4(a))
    elif b == 5:
        a = float(input("a= "))
        print(func_5(a))
    elif b == 6:
        a = float(input("a= "))
        print(func_6(a))
    elif b == 7:
        a = float(input("a= "))
        print(func_7(a))
    elif b == 8:
        a = float(input("a= "))
        print(func_8(a))
    elif b == 9:
        a = float(input("a= "))
        print(func_9(a))
    elif b == 10:
        a = float(input("a= "))
        print(func_10(a))
    elif b == 11:
        a = float(input("a= "))
        print(func_11(a))
    elif b == 12:
        a = float(input("a= "))
        print(func_12(a))
    else:
        if b == 0:
            break

            



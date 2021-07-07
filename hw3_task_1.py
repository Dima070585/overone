while True:
    x = int(input("x= "))
    y = int(input("y= "))
    sign = input("знак операции ")
    z = 0
    if sign == "0":
        break
    elif sign == "+":
        z = x + y
        print("z =",z)
    elif sign == "-":
        z = x - y
        print("z =", z)
    elif sign == "/":
        if y == 0:
            print("error")
        else:
            z = x / y
            print("z =", z)
    elif sign == "*":
        z = x * y
        print("z =", z)
    else:
        print("неверный знак операции")

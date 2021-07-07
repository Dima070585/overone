
def my_decor(func):
    def wrapper(*args):
        print('список')
        return func(*args[::-1])
    return wrapper
@ my_decor
def my_func1(a,b):
    return a-b
print(my_func1(1,2))
@ my_decor
def my_func2(a,b,c,d,e):
    return a+b+c+d-e
print(my_func2(1,2,3,4,5))
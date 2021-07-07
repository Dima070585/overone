from random import randint as r
a = [r(1, 10) for i in range(10)]
def my_decor(func):
    def wrapper(arg):
        print('список')
        print(a)
        arg = [i for i in a if i%2!=0]
        return func(arg)
    return wrapper
@ my_decor
def my_func(a):
    print(a)
my_func(a)
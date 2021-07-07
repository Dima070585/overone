a = input('введите слово: ')
b = input()
#a = ['шалаш','стол','дом']
from collections import counter
def pol(a):

    b=a[::-1]
    print(b)
    if a == b:
        print('полиндром')
        return a
def anogram(a,b):
    return counter(a)==counter(b)



print(pol(a))

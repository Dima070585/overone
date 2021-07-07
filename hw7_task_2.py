a = {' 1':5,'2':5,'333':5}
print(a)
dict1 = {key*2:value for key, value in a.items()}
print(dict1)
func = map(lambda x:x*2,a)
b = [1,2,3]
func1 = (lambda a:{k*2:v for k, v in a.items()})
print(type(a))
print(type(b))
print(func1)
print(list(func))
func = lambda **kwargs:{key*2:i for key, i in kwargs.items()}
print(func)
import math
def student(a,b,c):
    r = math.ceil(a/2) + math.ceil(b/2) + math.ceil(c/2)
    return r
print(student(25,27,30))
a = int(input("a= "))
s = 0
d = 1
while a>0:
    digit = a%10
    s = s + digit
    d = d * digit
    a = a // 10
print("s=",s)
print("d=",d)

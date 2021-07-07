a = []
s = 0
rez = 0
with open('f5.txt','r', encoding='utf_8') as f:
    for i,elem in enumerate(f.readlines()):
        b = elem
        a = elem.split(' ')
        s += int(a[1])
    rez = s/(i+1)
    print(s)
    print(rez)
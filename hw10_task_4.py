a=[]
b = ""
c = 0
d = 0
with open('f4.txt','r', encoding='utf_8') as f:
    for i,elem in enumerate(f.readlines()):
        b = elem
        a = elem.split(' ')
        c = len(a)

        d = len(b) - c + 1

        print(f'{elem} - {d} буквы, {c} слова')

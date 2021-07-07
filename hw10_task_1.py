n = int(input())
with open('f1.txt','w', encoding='utf_8') as f:
    for i in range(n):
        f.write(input() + '\n')


a = ['hello','world','!!!']
print(a)
for j in range(len(a)):
    j+=1
    b = [f'{j}-{i}' for i in a]
    print(b[j-1])
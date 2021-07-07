with open('f1.txt','r') as f1, open('f2.txt','w') as f2:
    for i,elem in enumerate(f1.readlines()):
        if i%2!=0:
            f2.write(elem)
with open('f1.txt','r') as f1, open('f3.txt','w') as f3:
    for i,elem in enumerate(f1.readlines()):
        if i%2==0:
            f3.write(elem)

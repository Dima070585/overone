import csv
with open('1.csv','r') as f, open('2.csv','w') as f1:
    reader = csv.reader(f)
    writer = csv.writer(f1)
    #for i in reader:
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0

    for i in reader:
        if 1<=int(i[2])<=15:
            a +=1
        if 13 <= int(i[2]) <= 18:
            b += 1
        if 19 <= int(i[2]) <= 25:
            c += 1
        if 26 <= int(i[2]) <= 40:
            d += 1
        if int(i[2])>= 40:
            e += 1
    writer.writerows([['1-12: ',a],
                      ['13-18: ',b],
                      ['19-25: ', c],
                      ['26-40: ', d],
                      ['40+: ', e]])

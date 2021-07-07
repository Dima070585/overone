sum_rezult= []
for n in range(200,301):
    rezult=[]
    i=1
    while i<n:
        if n%i==0:
            divider=n/i
            rezult.append(divider)
            i+=1
        else:
            i+=1
    sum_rezult.append(sum(rezult))


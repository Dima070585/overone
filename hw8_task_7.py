a = [1,2,3,4,5,6,7]


def tas_7(lst):
    for i in range(0,len(lst)-1,2):
        lst[i],lst[i+1] = lst[i+1],lst[i]
    return lst
print(tas_7(a))
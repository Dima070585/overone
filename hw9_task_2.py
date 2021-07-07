import copy
def task_2(str):
    a = []
    b = str.split(' ')
    a = copy.copy(b)
    print(b)
    for i in range(len(b)):
        for j in b[i]:
            if j.isdigit():
                a.remove(b[i])
    return a
print(task_2('bgc +3bn gdfHg 3-cvf MNH'))
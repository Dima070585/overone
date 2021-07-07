def task_3(a,b):
    if a == 0 or b == 0:
        return max(a,b)
    else:
        if a>b:
            print(a)
            return task_3(a-b,b)
        else:
            print(b)
            return task_3(a,b-a)
print(task_3(18,30))

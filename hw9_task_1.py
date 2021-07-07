def func(str):
    a = ''
    for i in str:
        if i.islower():
            a += i
    return a
print(func('fRT123 lkjdoPLmnTR'))

def sort(lst):
    rezult = {}
    for elem in list:
        new_lst = elem.split(' ')
        if new_lst[0] not in rezult:
            rezult[new_lst[0]] = None

    for key in rezult:
        key_result = {}
        for i in lst:
            elem = i.split(' ')
            if elem[0] == key and elem[1] not in key_result:
                key_result[elem[1]] = int(elem[2])
            elif elem[0] == key and elem[1] in key_result:
                key_result[elem[1]] += int(elem[2])
        key_list = [f'{k}{v}' for k,v in key_result.items()]
        key_list = sorted(key_list)
        rezult[key] = ' '.join(key_list)
    return rezult
lst = ['ivanov paper 10', 'petrov pens 5']
print(sort(lst))
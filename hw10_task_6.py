import json
a = []
b = ''
with open('f5.txt','r',encoding='utf_8' ) as f1, open('f6.json','w' ) as f2:
    f1 = f1.readlines()
    lst = []
    for string in f1:
        tmp_dict = {}
        string = string.split(' ')
        tmp_dict['name'] = string[0]
        tmp_dict['rate'] = int(string[1].replace('\n',''))
        lst.append(tmp_dict)
    json.dump(lst,f2,indent=4,)




